{{
  config(
    materialized="table"
  )
}}

select
    maintenance_id,
    incident_id,
    equipment_id,
    intervention_time,
    duration,
    result,
    cost
from {{ ref('stg_maintenance') }}
