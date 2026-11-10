{{
  config(
    materialized="view"
  )
}}

with incidents as (
    select * from {{ ref('stg_incidents') }}
),

equipments as (
    select * from {{ ref('stg_equipments') }}
)

select
    i.incident_id,
    i.equipment_id,
    i.incident_type,
    i.severity,
    i.start_time,
    i.end_time,
    i.status,
    e.site_id,
    e.equipment_type,
    e.manufacturer,
    e.equipment_criticality
from incidents as i
left join equipments as e on i.equipment_id = e.equipment_id
