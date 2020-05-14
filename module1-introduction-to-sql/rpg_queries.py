# app/chinook_queries.py
import os
import sqlite3
# IF DB IS IN SAME DIR AS THIS SCRIPT
DB_FILEPATH = os.path.join(os.path.dirname(__file__), "rpg_db.sqlite3")


# app/chinook_queries.py
##import os
##import sqlite3
# IF DB IS IN "DATA" DIR AND THIS FILE IS IN THE "APP: DIR:
#DB_FILEPATH = "data/chinook.db" 
#DB_FILEPATH = "data\chinook.db"
##DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data", "chinook.db")


connection = sqlite3.connect(DB_FILEPATH)
#connection.row_factory = sqlite3.Row

cursor = connection.cursor()

query = '''
select COUNT(distinct character_id)
from charactercreator_character;

select COUNT (distinct character_ptr_id) 
from charactercreator_mage;

select COUNT (distinct character_ptr_id) 
from charactercreator_fighter;

select COUNT (distinct character_ptr_id) 
from charactercreator_cleric;

select COUNT (distinct character_ptr_id) 
from charactercreator_thief;

select COUNT (distinct id) 
from charactercreator_character_inventory;

select COUNT (distinct item_id) 
from armory_item i;

select COUNT (distinct item_ptr_id) 
from armory_weapon w;

-- 37/174 is weapons:total_items

select
 count(id) as num_of_items,
  character_id
from charactercreator_character_inventory 
GROUP by character_id;

--this will satisfy both questions:how many items/weapons does each have
SELECT 
  ch.character_id
  ,ch."name" as char_name 
  ,count (distinct inv.item_id)
  ,count (distinct w.item_ptr_id) as weapon_id
FROM charactercreator_character ch
LEFT JOIN charactercreator_character_inventory inv ON ch.character_id = inv.character_id
LEFT JOIN armory_weapon w ON inv.item_id = w.item_ptr_id
group by ch.character_id;

select avg(item_count) as avg_items_per_char 
from (
 	select
 	 c.character_id,
 	  COUNT(distinct i.item_id) as item_count
 	from charactercreator_character c
 	join charactercreator_character_inventory i on c.character_id = i.character_id 
 	group by c.character_id
 ) subq1;

SELECT avg(weapon_count) as avg_weapons_per_char
FROM (
    SELECT 
      c.character_id
      ,c.name 
      ,count(distinct w.item_ptr_id) as weapon_count 
    FROM charactercreator_character c
    LEFT JOIN charactercreator_character_inventory i ON c.character_id = i.character_id
    LEFT JOIN armory_weapon w ON i.item_id = w.item_ptr_id
    GROUP BY c.character_id
) subq2;
'''

result2 = cursor.execute(query).fetchall()
print("RESULT 2", result2)

for row in result2:
    print(row)