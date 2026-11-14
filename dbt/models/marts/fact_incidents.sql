{{
  config(
    materialized="table"
  )
}}

select
    incident_id,
    equipment_id,
    incident_type,
    severity,
    start_time,
    end_time,
    status,
    site_id,
    equipment_type,
    manufacturer,
    equipment_criticality,
    case
        when end_time is not null and start_time is not null
            then DATE_PART('epoch', end_time - start_time) / 3600
    end as duration_hours
from {{ ref('int_incidents_enriched') }}
