SELECT COUNT(DISTINCT star_system) AS withs
FROM stations;

SELECT COUNT(*) AS without
FROM star_systems
WHERE system_name NOT IN (SELECT DISTINCT star_system FROM stations);