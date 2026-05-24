-- DIA UNO Empresas — generic private memory runtime
-- Purpose: baseline Supabase/Postgres schema for any private company instance.
-- Review before applying. Do not store secrets in this migration.

create schema if not exists gbrain;
create extension if not exists vector;
create extension if not exists pgcrypto;

create table if not exists gbrain.companies (
  id uuid primary key default gen_random_uuid(),
  slug text not null unique,
  name text not null,
  status text not null default 'active',
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table if not exists gbrain.operational_items (
  id uuid primary key default gen_random_uuid(),
  company_id uuid not null references gbrain.companies(id) on delete cascade,
  item_type text not null check (item_type in ('context_packet', 'statechange', 'receipt', 'decision', 'source', 'approval_boundary')),
  title text not null,
  body text not null,
  source text not null,
  owner text not null,
  freshness text not null default 'current',
  allowed_actions text[] not null default '{}',
  forbidden_actions text[] not null default '{}',
  required_approvals text[] not null default '{}',
  expected_outcome text,
  evidence_uri text,
  embedding vector(1024),
  metadata jsonb not null default '{}'::jsonb,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create index if not exists operational_items_company_type_idx
  on gbrain.operational_items(company_id, item_type);

create index if not exists operational_items_metadata_idx
  on gbrain.operational_items using gin(metadata);

create index if not exists operational_items_embedding_idx
  on gbrain.operational_items using ivfflat (embedding vector_cosine_ops)
  with (lists = 100);

create table if not exists gbrain.agent_access_log (
  id uuid primary key default gen_random_uuid(),
  company_id uuid references gbrain.companies(id) on delete cascade,
  agent_name text not null,
  surface text not null,
  action text not null,
  item_id uuid references gbrain.operational_items(id) on delete set null,
  approval_ref text,
  evidence_uri text,
  created_at timestamptz not null default now()
);

alter table gbrain.companies enable row level security;
alter table gbrain.operational_items enable row level security;
alter table gbrain.agent_access_log enable row level security;

-- Policies are intentionally conservative templates.
-- Replace `gbrain_agent` with the runtime DB role used by the private instance.
do $$
begin
  if exists (select 1 from pg_roles where rolname = 'gbrain_agent') then
    drop policy if exists gbrain_agent_companies_all on gbrain.companies;
    create policy gbrain_agent_companies_all
      on gbrain.companies
      for all
      to gbrain_agent
      using (true)
      with check (true);

    drop policy if exists gbrain_agent_operational_items_all on gbrain.operational_items;
    create policy gbrain_agent_operational_items_all
      on gbrain.operational_items
      for all
      to gbrain_agent
      using (true)
      with check (true);

    drop policy if exists gbrain_agent_access_log_all on gbrain.agent_access_log;
    create policy gbrain_agent_access_log_all
      on gbrain.agent_access_log
      for all
      to gbrain_agent
      using (true)
      with check (true);
  end if;
end $$;
