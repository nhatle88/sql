sql = "select t.description, b.name, t.created \
        from building as b right join ticket as t on b.id = t.building_id \
        where b.name = '"+ building_selected +"'"
        
df = pd.read_sql(sql, conn)
df_grouped_date = df.groupby('date').count().reset_index()
df_grouped_building = df.groupby('name').count().reset_index().sort_values(by=['created'])

building_hiddenlist = "('Empty Building','Serenity Sky Villas')"
sql = "select t.description, b.name, rt.rating, rt.created, rt.review \
        from rating_ticket rt \
            left join ticket t on rt.ticket_id = t.id \
            left join building b on t.building_id = b.id \
        where b.name NOT IN {}".format(building_hiddenlist)
        
        
# check null
pd.isna(df['column'])
