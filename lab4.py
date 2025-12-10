import time
import sys

items = [
    ("吸入器","i", 1 , 5 ),("步枪","r", 3 , 25 ),("手枪","p", 2 , 15 ),
    ("弹药","a", 2 , 15 ),("急救箱","m", 2 , 20 ),("刀","k", 1 , 15 ),
    ("斧头","x", 3 , 20 ),("护身符","t", 1 , 25 ),("烧瓶","f", 1 , 15 ),
    ("解药","d", 1 , 10 ),("食物","s", 2 , 20 ),("弓弩","c", 2 , 20 )
]


def method():
    package = 9
    used_space = 0
    total_points = 10
    final_item = []
    final_item_name = []
    table = []

    new_items = sorted(items, key=lambda x: x[3]/x[2], reverse=True)

    print(f'\n{"特殊情况： "}')
    print(f'{"哮喘！！"}')
    print()
    items.remove(("吸入器","i", 1, 5))
    package = package -1
    for item in new_items:
        name,number,size,points = item
        if used_space + size <= package:
            used_space += size
            total_points += points
            final_item.append(item) 
            final_item_name.append(item[0])
    for item_x in final_item:
        new_items.remove(item_x)
            
    for no_items in new_items:
        name_2,number_2,size_2,points_2 = no_items
        total_points -= points_2         

    final_item.append(("吸入器","i", 1 , 5 ))
    final_item_name.append("吸入器")        
    total_points += 5
    print(f'{final_item_name}\n')


    for item in final_item:
        for _ in range(int(item[2])):
            table.append(f"[{item[1]}]")
    print(f'{table[:3]}')
    print(f'{table[3:6]}')
    print(f'{table[6:9]}\n')    

    print(f"总分数: {total_points}\n")


    if total_points < 0 :
        print(f"你毫无生还可能.....")
    elif total_points == 0:
        print(f" 你活下来了，只是非常艰难...") 
    elif total_points > 0 :
        print(f"你成功存活！！")      
    print(f"THE END")



print(f"正在生成末日环境")
method()