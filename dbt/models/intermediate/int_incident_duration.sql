{{
  config(
    materialized="view"
  )
}}

select
    incident_id,
    equipment_id,
    start_time,
    end_time,
    case
        when end_time is not null and start_time is not null
            then DATE_PART('epoch', end_time - start_time) / 3600
    end as duration_hours
from {{ ref('stg_incidents') }}
