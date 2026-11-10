{{
  config(
    materialized="view"
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
from {{ ref('maintenance') }}
