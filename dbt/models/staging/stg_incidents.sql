{{
  config(
    materialized="view"
  )
}}

select
    incident_id,
    equipment_id,
    incident_type,
    severity,
    start_time,
    end_time,
    known_cause,
    status
from {{ ref('incidents') }}
