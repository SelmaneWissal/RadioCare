{{
  config(
    materialized="table"
  )
}}

with equipment_incidents as (
    select
        equipment_id,
        count(*) as incident_count,
        count(case when status = 'Cloturé' then 1 end)
            as resolved_incident_count,
        count(case when status in ('Ouvert', 'En cours') then 1 end)
            as open_incident_count,
        max(start_time) as last_incident_time
    from {{ ref('fact_incidents') }}
    group by equipment_id
),

equipment_availability as (
    select
        equipment_id,
        avg(availability_score) as avg_availability_score
    from {{ ref('fact_availability') }}
    group by equipment_id
)

select
    e.equipment_id,
    e.site_id,
    e.equipment_type,
    e.manufacturer,
    e.installation_date,
    e.equipment_criticality,
    ei.last_incident_time,
    ea.avg_availability_score,
    coalesce(ei.incident_count, 0) as incident_count,
    coalesce(ei.resolved_incident_count, 0) as resolved_incident_count,
    coalesce(ei.open_incident_count, 0) as open_incident_count,
    case
        when ei.open_incident_count > 0 then 'Prioritaire'
        when ei.incident_count >= 3 then 'Surveillé'
        else 'Stable'
    end as priority_level
from {{ ref('stg_equipments') }} as e
left join equipment_incidents as ei on e.equipment_id = ei.equipment_id
left join equipment_availability as ea on e.equipment_id = ea.equipment_id
