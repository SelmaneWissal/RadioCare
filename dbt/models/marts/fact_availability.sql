{{
  config(
    materialized="table"
  )
}}

select
    equipment_id,
    event_time,
    signal_level,
    temperature,
    error_rate,
    availability_status,
    case
        when availability_status = 'Disponible' then 1
        when availability_status = 'Degradé' then 0.5
        else 0
    end as availability_score
from {{ ref('stg_telemetry') }}
