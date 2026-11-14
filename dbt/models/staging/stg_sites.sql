{{
  config(
    materialized="view"
  )
}}

select
    site_id,
    site_name,
    region,
    site_category,
    criticality
from {{ ref('sites') }}
