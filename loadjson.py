import json
from glob import glob


def main():

    dict = {}

    for file in glob('./json/*.json'):

        with open(file, 'r', encoding='utf8') as f:
            data = json.load(f)

            try:
                # print(data['name'], data['rating'], data['user_ratings_total'])
                dict[data['place_id']] = [data['name'],
                                          data['rating'], data['user_ratings_total']]
            except:
                # print(data['name'])
                dict[data['place_id']] = [data['name'], 0, 0]

    # sort dict in place by rating from small to large and secondly by user_ratings_total from large to small
    dict = sorted(dict.items(), key=lambda x: (x[1][1], x[1][2]), reverse=True)

    # dict = sorted(dict.items(), key=lambda x: x[1][1], reverse=False)
    # print data
    for key, value in dict:
        print(key, value[0], value[1], value[2])

    # output dict as csv
     
    with open('output.csv', 'w', encoding='utf8') as f:
        f.write("place_id,name,rating,user_ratings_total\n")
        for key, value in dict:
            f.write("%s,%s,%s,%s\n" % (key, value[0], value[1], value[2]))

    
    


if __name__ == '__main__':
    main()
