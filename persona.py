import facebook
import json

def updateProfile(access_token, conn):
    graph = facebook.GraphAPI(object)
    profile = graph.get_object("me")
    interests = graph.get_connections(id="me", connection_name="likes")['data']
    likes = None
    for i in interests:
        if (likes is None):
            likes = i['category']
        else:
            likes = likes + '/' + i['category']


    formatted_profile = json.dumps(profile)
    profile_load = json.loads(formatted_profile)
    location = profile_load['location']['name']
    homeTown = profile_load['hometown']['name']
    school = profile_load['education']
    education = profile_load['education'][len(school)-1]['type']
    work = profile_load['work']
    if not (work is None):
        isProfessional = '1'

    x = conn.cursor()
    result = None
    try:
        result = x.execute("SELECT facebookid from PERSONS where facebookid=%s",profile_load['id'])

    except Exception as e:
        #print e
        conn.rollback()


    if (result is None):
        try:
           x.execute("""INSERT
           INTO
           `kendb`.
           `PERSONS`
           (
               `deviceid`,
               `number`,
               `dob`,
               `city`,
               `state`,
               `zipcode`,
               `education`,
               `gender`,
               `facebookid`,
               `civil`,
               `kids`,
               `email`,
               `isProfessional`,
               `hometown_state`,
               `interests`
               )
           VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                     ('1',
               '2241211212',
               profile_load['birthday'],
               location.split(',')[0],
               location.split(',')[1],
           '43016',
           education,
           profile_load['gender'],
           profile_load['id'],
            profile_load['relationship_status'],
           '1',
           profile_load['email'],
           isProfessional,
           homeTown.split(',')[1],
           likes))

           conn.commit()
        except Exception as e:
            #print e
            conn.rollback()
    else:
        try:
            result2 = x.execute("""UPDATE
                   `kendb`.
                   `PERSONS`
                   SET
                    `deviceid` = %s,
                    `number` = %s,
                    `dob` = %s,
                    `city` = %s,
                    `state` = %s,
                    `zipcode` = %s,
                    `education` = %s,
                    `gender` = %s,
                    `facebookid` = %s,
                    `civil` = %s,
                    `kids` = %s,
                    `email` = %s,
                    `isProfessional` = %s,
                    `hometown_state` = %s,
                    `interests` = %s
                    WHERE `facebookid` = %s""",
                               ('3',
                                '2241232323',
                                profile_load['birthday'],
                                location.split(',')[0],
                                location.split(',')[1],
                                '43016',
                                education,
                                profile_load['gender'],
                                profile_load['id'],
                                profile_load['relationship_status'],
                                '2',
                                profile_load['email'],
                                isProfessional,
                                homeTown.split(',')[1],
                                likes,
                                profile_load['id']))
            conn.commit()
        except Exception as e:
            #print e
            conn.rollback()

    return profile_load['id']
