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
    criticality
from {{ source('raw', 'equipments') }}
