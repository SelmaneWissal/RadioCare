{{
  config(
    materialized="view"
  )
}}

select
    equipment_id,
    site_id,
    equipment_type,
    manufacturer,
    installation_date,
    criticality as equipment_criticality
from {{ ref('equipments') }}
