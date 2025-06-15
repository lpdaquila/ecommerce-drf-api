SELECT DISTINCT p.id, p.name, p.codename
FROM "users_usergroup" AS ug

JOIN "users_grouppermissions" AS ugp ON ug.group_id = ugp.group_id
JOIN "auth_permissions" AS p ON ugp.permission_id = p.id

WHERE ug.id = %d