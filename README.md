# Some SQL code

### 1. Use format and variable at the same time
```python
tb_user = '"user"'
sql = "select b.name, c.created, c.name as company_name, u.fullname \
        from building as b \
            left join company as c on b.company = c.id \
            right join {user} as u on b.company = u.company \
        where b.name = '".format(user = tb_user) + building_selected +"'"
```
