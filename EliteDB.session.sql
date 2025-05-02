DELETE FROM stations
WHERE (station_name, star_system) IN (
  SELECT station_name, star_system
  FROM stations
  GROUP BY station_name, star_system
  HAVING COUNT(*) > 1
)
AND id NOT IN (
  SELECT MIN(id)
  FROM stations
  GROUP BY station_name, star_system
);