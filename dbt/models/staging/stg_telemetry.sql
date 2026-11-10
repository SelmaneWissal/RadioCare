{{
  config(
    materialized="view"
  )
}}

select
    event_id,
    equipment_id,
    event_time,
    signal_level,
    temperature,
    error_rate,
    availability_status
from {{ source('raw', 'telemetry') }}
