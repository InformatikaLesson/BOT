import discord
import asyncio
from discord.ext import commands
import random
import datetime
from PIL import Image
#from itertools import cycle

## CUSTOM library
#from Bot_classes import Profile, Roulette, Shop, Quest
from Buildings import Building, Tavern, Blockpost, Market, Altar, WoodHarvester, Sawmill, StoneHarvester
from Buildings import IronMine, SilverMine, GoldMine, RubbiesMine, DiamondsMine, Smelter
from Buildings import Storage, Calculator
from Lottery import Lottery
from Castle import Castle
## ~~~~~~~~

## MYSQL DATABASE
import pymysql.cursors
# INIT mysql
#mydb = pymysql.connect(host="localhost", user="root", password = "mysqlforbot426", database="memesandspeak_bot_database",)
#my_cursor = mydb.cursor()
## ~~~~~~~~~~~~~~


#bot_channel = discord.abc.Messageable
bot = commands.Bot(command_prefix="!")
# REMOVING standartised '!help'
bot.remove_command("help")
TOKEN = "NTU1MTA3MjU0ODE5NjE4ODI2.D2mYZw.F_Bvx_Hfc3wh6GoaDk42uNtil4k"

############   ALL PROFILES   ###
global_members_dic = {}

# Bot version/update time:
bot_version = '0.05 (in developing)'
########################### y \\ m \\ d #
#update_date = datetime.date(2019, 4, 28)
update_date = datetime.datetime.now()
date_formatted = update_date.strftime("%A %d. %B %Y")
# Footer information:
bot_version = "Current bot version: {ver} • Last update: {date}".format(ver=bot_version, date=date_formatted)
bot_picture = "http://simpleicon.com/wp-content/uploads/wrench.png"

# Images for uploading:
img_elon_musk_path = "Pictures/Elon Musk (weed).jpg"
img_anton_path = "Pictures/Антон (СЕКС).jpg"
img_elon_musket_path = "Pictures/Elon Musket.jpg"
img_gloria_borger_path = "Pictures/Gloria_Borger.jpg"
img_dudec_path = "Pictures/Дудец.jpg"
img_mafiosnik_path = "Pictures/Мафиозник.jpg"
img_momo_path = "Pictures\момо.jpg"
img_old_path = "Pictures/олд.jpg"
img_pooovar_path = "Pictures/Пооовар.jpg"
img_ystavwii_alexeenko_path = "Pictures/Уставший Алексеенко.jpg"
#
img_lottery_path = "Pictures/Три_лотерейных_билета.jpg"




#####################################################################################################################
#####################################################################################################################
## logging utility
def _logging(event_to_logg, end_line=True):
        ''' must contain information which will be logged in var "event_to_logg"
        If var "end_line" was modified to 'False' does not finish each line with '\n' '''

        try:
            with open("loggs.txt", "a") as f:
                logg_msg = f"[{str(datetime.datetime.now())[:-7]}]: {event_to_logg}"
                if end_line:
                    logg_msg += "\n"
                f.write(logg_msg)
        except Exception as e:
            print(f"Error in '_logging' function: {e}")

## Players issues utility
def _write_an_issue(issue):

        try:
            with open("issue.txt", "a") as f:
                logg_msg = f"[{str(datetime.datetime.now())[:-7]}]: {issue}\n"
                f.write(logg_msg)
        except Exception as e:
            print(f"Error in '_issue' function: {e}")

#####################################################################################################################
#####################################################################################################################


########################################                    #####################################
########################################       EVENTS       #####################################
########################################                    #####################################
## MYSQL utility
async def connect_to_mysql():
    global mydb, my_cursor
    await bot.wait_until_ready()

    while not bot.is_closed():
        ## Connect to database
        mydb = pymysql.connect(host="localhost", user="root", password="mysqlforbot426", database="memesandspeak_bot_database", )
        my_cursor = mydb.cursor()
        ## Wait an hour
        await asyncio.sleep(3600)
        ## Close database
        mydb.close()


## Every hour debit/credit calculation
async def calculate_every_hour():
    global mydb, my_cursor
    await bot.wait_until_ready()

    while not bot.is_closed():

        ## Wait an hour
        await asyncio.sleep(3600)

        do_not_logg = False
        ## REPORT datetime - 1
        date1 = datetime.datetime.now()
        ## DATA
        tmp = "SELECT * FROM buildings"
        my_cursor.execute(tmp)
        all_buildings_info = my_cursor.fetchall()
        data_dic = {}
        for each_building in all_buildings_info:

            #
            if each_building[2] == "Таверна":
                actuall_building_class = Tavern()
            elif each_building[2] == "Пост Охраны":
                actuall_building_class = Blockpost()
            elif each_building[2] == "Рынок":
                actuall_building_class = Market()
            elif each_building[2] == "Алтарь Веры":
                actuall_building_class = Altar()
            elif each_building[2] == "Дровосек":
                actuall_building_class = WoodHarvester()
            elif each_building[2] == "Лесопилка":
                actuall_building_class = Sawmill()
            elif each_building[2] == "Камнетёс":
                actuall_building_class = StoneHarvester()
            elif each_building[2] == "Железная шахта":
                actuall_building_class = IronMine()
            elif each_building[2] == "Серебряная шахта":
                actuall_building_class = SilverMine()
            elif each_building[2] == "Золотая шахта":
                actuall_building_class = GoldMine()
            elif each_building[2] == "Шахта рубинов":
                actuall_building_class = RubbiesMine()
            elif each_building[2] == "Алмазная шахта":
                actuall_building_class = DiamondsMine()
            elif each_building[2] == "Плавильня":
                actuall_building_class = Smelter()
            elif each_building[2] == "Городской склад":
                actuall_building_class = Storage()
            #
            if issubclass(type(actuall_building_class), Building):
                if each_building[3] == 2:
                    actuall_building_class._get_lvl_2
                elif each_building[3] == 3:
                    actuall_building_class._get_lvl_3
                elif each_building[3] == 4:
                    actuall_building_class._get_lvl_4
                elif each_building[3] == 5:
                    actuall_building_class._get_lvl_5
            else:
                if each_building[3] != 1:
                    lvl = each_building[3]
                    actuall_building_class.get_level(lvl)
            #
            try:
                discord_id = each_building[1]
                str_key = str(discord_id)
                buildings_list = data_dic[str_key]
                buildings_list.append(actuall_building_class)
                data_dic[str_key] = buildings_list
            except:
                data_dic[str_key] = [actuall_building_class]

        #print("Entering calculator with data: ", data_dic)
        ## Creating calculator
        calculator = Calculator()

        for each_key in list(data_dic.keys()):
            if len(list(data_dic.keys())) == 0:
                do_not_logg = True
                break
            #
            buildings_list = data_dic[each_key]
            # Calculation #######
            result_dic = calculator.calculate_income(buildings_list)
            #####################

            ### CHECK HOW MUCH MONEY
            value = result_dic["money"]
            my_cursor.execute(f"SELECT money FROM profile_data WHERE discord_id = {each_key}")

            ### calculating current money
            money = my_cursor.fetchall()[0][0]
            money += value

            ### UPDATE MONEY
            mysql_input = f"UPDATE profile_data SET money = {money} WHERE discord_id = {each_key}"
            my_cursor.execute(mysql_input)
            mydb.commit()

            all_keys = result_dic.keys()
            for new_key in all_keys:
                if new_key != "money":
                    ### CHECK HOW MUCH RESOURCE
                    value = result_dic[new_key]
                    my_cursor.execute(f"SELECT {new_key} FROM capital_storage WHERE discord_id = {each_key}")

                    ### calculating current resource
                    resource = my_cursor.fetchall()[0][0]
                    resource += value

                    ### UPDATE RESOURCE
                    mysql_input = f"UPDATE capital_storage SET {new_key} = {resource} WHERE discord_id = {each_key}"
                    my_cursor.execute(mysql_input)
                    mydb.commit()

        if not do_not_logg:
            ## REPORT datetime - 2 AND timedelta
            date2 = datetime.datetime.now()
            delta_perfomance = date2 - date1
            ### DO LOGGING WITH DELTA PERFOMANCE
            _logging(f"Hourly event 'calculation of income/charge' was finished succesfuly with time perfomance [{delta_perfomance}].")



#####################################################################################################################
#####################################################################################################################
########################################        ########### ########## ########### ######## ########## ######### ####

#### Inventory embed
def _set_inventory_embed(id_of_user, discord_user):
    global global_members_dic
    unit = global_members_dic[str(id_of_user)]
    #
    my_cursor.execute(f"SELECT * FROM date_database WHERE discord_id = {discord_id}")
    result_date = my_cursor.fetchall()[0][1]
    ###
    #Embed
    colour = discord.Color.dark_gold()
    #
    em_title = f"ИНВЕНТАРЬ ({unit.name})"
    data = unit._return_my_inv()
    #
    info_msg = discord.Embed(description=data, colour=colour)
    info_msg.set_author(name=em_title)
    #
    ####### ADD SOME STUFF
    #
    date_time = result_date
    date_formatted_1 = date_time.strftime("%A %d. %B %Y")
    footer_text = f"В игре с {date_formatted_1}."
    info_msg.set_footer(text=footer_text, icon_url=bot_picture)
    #
    return info_msg


## update embed
def _set_update_embed_(discord_id, discord_user, buildings_data, building):
    '''

    :param discord_id: user's id
    :param discord_user: user
    :param buildings_data: all data with buildings of same class
    :param building: actual building's class
    :return: sets and returns embed msg for '!улучшить' bot command
    '''
    ####### UTILITY FUNCTION, to copy building type:
    #
    def _copy_function(building):
        if building.name == "Таверна":
            actuall_building_class = Tavern()
        elif building.name == "Пост Охраны":
            actuall_building_class = Blockpost()
        elif building.name == "Рынок":
            actuall_building_class = Market()
        elif building.name == "Алтарь Веры":
            actuall_building_class = Altar()
        elif building.name == "Дровосек":
            actuall_building_class = WoodHarvester()
        elif building.name == "Лесопилка":
            actuall_building_class = Sawmill()
        elif building.name == "Камнетёс":
            actuall_building_class = StoneHarvester()
        elif building.name == "Железная шахта":
            actuall_building_class = IronMine()
        elif building.name == "Серебряная шахта":
            actuall_building_class = SilverMine()
        elif building.name == "Золотая шахта":
            actuall_building_class = GoldMine()
        elif building.name == "Шахта рубинов":
            actuall_building_class = RubbiesMine()
        elif building.name == "Алмазная шахта":
            actuall_building_class = DiamondsMine()
        elif building.name == "Плавильня":
            actuall_building_class = Smelter()
        elif building.name == "Городской склад":
            actuall_building_class = Storage()
        else:
            raise TypeError
        return actuall_building_class
    #
    my_cursor.execute(f"SELECT * FROM date_database WHERE discord_id = {discord_id}")
    result_date = my_cursor.fetchall()[0][1]
    ###

    ########################################
    def _get_this_lvl_stats(building, lvl):
        if issubclass(type(building), Building):
            if lvl == 2:
                building._get_lvl_2
            elif lvl == 3:
                building._get_lvl_3
            elif lvl == 4:
                building._get_lvl_4
            elif lvl == 5:
                building._get_lvl_5
        else:
            if lvl != 1:
                building.get_level(lvl)
            else:
                return
        #
        return building
    ########################################
    #print(buildings_data)
    main_txt = ""
    for each_building in buildings_data:
        #print(each_building)
        lvl = int(each_building[1])
        new_building = _copy_function(building)
        leveled_building = _get_this_lvl_stats(new_building, lvl)
        try:
            income = f"Прибыль здания: {leveled_building.income}$\n"
            charge = f"Оплата здания: {leveled_building.outcome}$\n"
        except Exception as e:
            income = ""
            charge = ""
            #print(e)
        try:
            resource = f"Количество добываемого ресурса: {leveled_building.resource_harvest} шт.\n"
        except Exception as e:
            resource = ""
            #print(e)
        try:
            storage = f"Количество хранимого ресурса: {leveled_building.resource_storage} шт."
        except Exception as e:
            storage = ""
            #print(e)


        info_list = [f"\n\n • {building.name} Ур.{lvl}\n",
                     f"Текущие характеристики:",
                     f"{income}{charge}{resource}{storage}"]
        info = "\n".join(info_list)
        main_txt += info
        ######### ######### ######### ######## ######### #########
        leveled_building = _get_this_lvl_stats(new_building, lvl+1)
        try:
            income = f"Прибыль здания: {leveled_building.income}$\n"
            charge = f"Оплата здания: {leveled_building.outcome}$\n"
        except Exception as e:
            income = ""
            charge = ""
            #print(e)
        try:
            resource = f"Количество добываемого ресурса: {leveled_building.resource_harvest} шт.\n"
        except Exception as e:
            resource = ""
            #print(e)
        try:
            storage = f"Количество хранимого ресурса: {leveled_building.resource_storage} шт."
        except Exception as e:
            storage = ""
            #print(e)
        #
        time = datetime.timedelta(seconds=leveled_building.time_to_build)
        #
        info_list = [f"\nХарактеристики после улучшения:",
                     f"{income}{charge}{resource}{storage}",
                     f"Цена улучшения: {leveled_building.cost}$",
                     f"Время улучшения: {time}"]
        info = "\n".join(info_list)
        main_txt += info

    #
    main_txt = f"**{main_txt}**"
    # Embed
    colour = discord.Color.dark_gold()
    #
    em_title = f"Улучшение здания 'Шахта рубинов'"
    #
    info_msg = discord.Embed(description=main_txt, colour=colour)
    info_msg.set_author(name=em_title)
    ####### ADD SOME STUFF
    odd_text = "Для улучшения здания введите текущий уровень того здания, которое желаете улучшить и подтвердите улучшение."
    info_msg.add_field(name="Помощь", value=odd_text, inline=False)
    ###
    #
    date_time = result_date
    date_formatted_1 = date_time.strftime("%A %d. %B %Y")
    footer_text = f"В игре с {date_formatted_1}."
    info_msg.set_footer(text=footer_text, icon_url=bot_picture)
    #
    return info_msg



#### Storage embed
def _set_storage_embed(discord_id, discord_user):

    ## DATA
    my_cursor.execute(f"SELECT * FROM capital_storage WHERE discord_id = {discord_id}")
    storage_data = my_cursor.fetchall()[0]
    wood, plank, stone, iron_ore, iron, silver_ore, silver, gold_ore, gold, rubbies, diamonds = storage_data[1:]
    #
    my_cursor.execute(f"SELECT current_storage, storage_capacity, capital_name FROM profile_data WHERE discord_id = {discord_id}")
    storage_info = my_cursor.fetchall()[0]
    current_storage, storage_capacity, capital_name = storage_info
    #
    my_cursor.execute(f"SELECT * FROM date_database WHERE discord_id = {discord_id}")
    result_date = my_cursor.fetchall()[0][1]
    ###
    ##
    # Embed
    colour = discord.Color.dark_gold()
    #
    em_title = f"ГОРОДСКОЙ СКЛАД ({capital_name})"
    #
    info_msg = discord.Embed(description="", colour=colour)
    info_msg.set_author(name=em_title)
    #
    ####### ADD SOME STUFF
    profile_data_list_raw = [f"дерево\t\t\t\t\t\t-\t\t\t{wood}", f"доски\t\t\t\t\t\t\t-\t\t\t{plank}",
                             f"камень\t\t\t\t\t\t-\t\t\t{stone}", f"железная руда\t\t\t-\t\t\t{iron_ore}",
                             f"железо\t\t\t\t\t\t-\t\t\t{iron}", f"серебряная руда\t\t-\t\t\t{silver_ore}",
                             f"серебро\t\t\t\t\t\t-\t\t\t{silver}", f"золотая руда\t\t\t-\t\t\t{gold_ore}",
                             f"золото\t\t\t\t\t\t-\t\t\t{gold}", f"рубины\t\t\t\t\t\t-\t\t\t{rubbies}",
                             f"диаманты\t\t\t\t\t-\t\t\t{diamonds}"]
    profile_data_list = "\n".join(profile_data_list_raw)
    profile_data_list = "**{}**".format(profile_data_list)
    info_msg.add_field(name="Ресурсы:\t\t\t\t\t\t\t шт.", value=profile_data_list, inline=False)
    #
    odd_text = f"Чтобы включить автоматическую продажу ресурсов введите команду '!автопродажа' (У вас должен быть построен рынок хотя бы 3 уровня)"
    odd_text = "**{}**".format(odd_text)
    info_msg.add_field(name="Автоматическая продажа ресурсов", value=odd_text, inline=False)
    ###
    date_time = result_date
    date_formatted_1 = date_time.strftime("%A %d. %B %Y")
    footer_text = f"В игре с {date_formatted_1}."
    info_msg.set_footer(text=footer_text, icon_url=bot_picture)
    #
    return info_msg


#### Capital embed
#def _set_capital_embed(discord_id, discord_user):
def _set_capital_embed(discord_id, discord_user):
    ####### UTILITY FUNCTION, to copy building type:
    #
    def _copy_function(building_name):
        if building_name == "Таверна":
            actuall_building_class = Tavern()
        elif building_name == "Пост Охраны":
            actuall_building_class = Blockpost()
        elif building_name == "Рынок":
            actuall_building_class = Market()
        elif building_name == "Алтарь Веры":
            actuall_building_class = Altar()
        elif building_name == "Дровосек":
            actuall_building_class = WoodHarvester()
        elif building_name == "Лесопилка":
            actuall_building_class = Sawmill()
        elif building_name == "Камнетёс":
            actuall_building_class = StoneHarvester()
        elif building_name == "Железная шахта":
            actuall_building_class = IronMine()
        elif building_name == "Серебряная шахта":
            actuall_building_class = SilverMine()
        elif building_name == "Золотая шахта":
            actuall_building_class = GoldMine()
        elif building_name == "Шахта рубинов":
            actuall_building_class = RubbiesMine()
        elif building_name == "Алмазная шахта":
            actuall_building_class = DiamondsMine()
        elif building_name == "Плавильня":
            actuall_building_class = Smelter()
        elif building_name == "Городской склад":
            actuall_building_class = Storage()
        else:
            raise TypeError
        return actuall_building_class

    ########################################
    def _get_this_lvl_stats(building, lvl):
        if issubclass(type(building), Building):
            if lvl == 2:
                building._get_lvl_2
            elif lvl == 3:
                building._get_lvl_3
            elif lvl == 4:
                building._get_lvl_4
            elif lvl == 5:
                building._get_lvl_5
        else:
            if lvl != 1:
                building.get_level(lvl)
            #else:
                #return
        #
        return building
    ### DATA
    my_cursor.execute(f"SELECT * FROM date_database WHERE discord_id = {discord_id}")
    result_date = my_cursor.fetchall()[0][1]
    ###
    tmp = f"SELECT capital_name, capital_castle_type, capital_castle_name, capital_max_buildings, capital_buildings FROM profile_data WHERE discord_id = {discord_id}"
    my_cursor.execute( tmp )
    profile_data = my_cursor.fetchall()
    ##
    tmp = f"SELECT * FROM buildings WHERE discord_id = {discord_id}"
    my_cursor.execute(tmp)
    buildings_data = my_cursor.fetchall()
    ###
    main_txt = f"{profile_data[0][1]} ({profile_data[0][2]})\nВ городе {profile_data[0][4]}/{profile_data[0][3]} строительных мест.\n" \
               f"Постройки:"
    main_txt = f"**{main_txt}**\n"
    #
    for each_building in buildings_data:
        new_building_name = each_building[2]
        lvl_building = each_building[3]
        new_building = _copy_function(new_building_name)
        new_building = _get_this_lvl_stats(new_building, lvl_building)
        tmp_txt = f"{new_building.name} ({lvl_building} уровня)\n"
        main_txt += tmp_txt
        #
    ### Embed
    colour = discord.Color.dark_gold()
    #
    em_title = f"{profile_data[0][0]}"
    #
    info_msg = discord.Embed(description=main_txt, colour=colour)
    info_msg.set_author(name=em_title)
    ####### ADD SOME STUFF
    odd_text = "Для улучшения города введите '!расширить'.\nЧтобы увидеть количество ресурсов введите '!склад'."
    info_msg.add_field(name="Помощь", value=odd_text, inline=False)
    ###
    #
    date_time = result_date
    date_formatted_1 = date_time.strftime("%A %d. %B %Y")
    footer_text = f"В игре с {date_formatted_1}."
    info_msg.set_footer(text=footer_text, icon_url=bot_picture)
    #
    return info_msg


#### Profile embed
def _set_profile_embed(id_of_user, discord_user):

    ## DATA
    my_cursor.execute(f"SELECT * FROM profile_data WHERE discord_id = {id_of_user}")
    result_profile_data = my_cursor.fetchall()[0]
    #
    my_cursor.execute(f"SELECT * FROM skills WHERE discord_id = {id_of_user}")
    result_skills = my_cursor.fetchall()[0]
    #
    my_cursor.execute(f"SELECT * FROM date_database WHERE discord_id = {id_of_user}")
    result_date = my_cursor.fetchall()[0]
    ###

    #Embed
    colour = discord.Color.dark_gold()
    if discord_user.display_name is not discord_user.name:
        tmp_nick = f"\nИмя на сервере:\t\t'{discord_user.display_name}'"
    else:
        tmp_nick = f""
    #
    em_title = f"ПРОФИЛЬ"
    info_msg = discord.Embed(description="", colour=colour)
    info_msg.set_author(name=em_title)
    #
    ####### ADD SOME STUFF
    profile_data_list_raw = [f"Пользователь:\t\t\t<@{id_of_user}>{tmp_nick}",
                             f"Государство:\t\t\t{result_profile_data[1]}",
                             f"Столица:\t\t\t\t\t{result_profile_data[5]}",
                             f"Тип столицы:\t\t\t{result_profile_data[12]}",
                             f"Класс столицы:\t\t{result_profile_data[11]}",
                             f"Построек:\t\t\t\t\t{result_profile_data[14]}/{result_profile_data[13]}",
                             f"Казна:\t\t\t\t\t\t\t{result_profile_data[7]}$"]
    profile_data_list = "\n".join(profile_data_list_raw)
    profile_data_list = "**{}**".format(profile_data_list)
    info_msg.add_field(name="Государство", value=profile_data_list, inline=False)
    #
    character_values_raw = [f"Имя:\t\t\t\t\t\t\t{result_profile_data[3]}",
                            f"Уровень:\t\t\t\t\t{int(result_skills[1])}  [{result_skills[2]}/{result_skills[3]}]",
                            f"Скилпоинты:\t\t\t\t{int(result_skills[4])}",
                            f"Вера:\t\t\t\t\t\t\t{int(result_profile_data[8])}",
                            f"Честь:\t\t\t\t\t\t\t{int(result_profile_data[9])}"]
    character_values = "\n".join(character_values_raw)
    character_values = "**{}**".format(character_values)
    info_msg.add_field(name="Персонаж", value=character_values, inline=False)
    #######
    date_time = result_date[1]
    date_formatted_1 = date_time.strftime("%A %d. %B %Y")
    footer_text = f"В игре с {date_formatted_1}."
    info_msg.set_footer(text=footer_text, icon_url=bot_picture)
    #
    return info_msg

#### Set building menu
def _set_building_menu(id_of_user, discord_user):

    # DATA
    my_cursor.execute(f"SELECT capital_buildings, capital_max_buildings FROM profile_data WHERE discord_id = {id_of_user}")
    buildings_info = my_cursor.fetchall()[0]
    buildings_built = buildings_info[0]
    buildings_max = buildings_info[1]
    #
    my_cursor.execute(f"SELECT * FROM date_database WHERE discord_id = {id_of_user}")
    result_date = my_cursor.fetchall()[0]
    ###

    ### Embed
    colour = discord.Color.dark_gold()
    em_title = f"МЕНЮ СТРОИТЕЛЬСТВА"
    info_text = f"**Инфо**: В вашей столице построено {buildings_built}/{buildings_max}\nДля начала строительства введите '!строить (здание)'"
    info_msg = discord.Embed(description=info_text, colour=colour)
    info_msg.set_author(name=em_title)

    ### TAVERN building
    tavern_info_raw = Tavern.info_list
    tavern_info = "\n".join(tavern_info_raw)
    info_msg.add_field(name="ТАВЕРНА (Ур.1)", value=tavern_info, inline=False)
    ### MARKET buidling
    market_info_raw = Market.info_list
    market_info = "\n".join(market_info_raw)
    info_msg.add_field(name="РЫНОК (Ур.1)", value=market_info, inline=False)
    ### BLOCKPOST building
    blockpost_info_raw = Blockpost.info_list
    blockpost_info = "\n".join(blockpost_info_raw)
    info_msg.add_field(name="ПОСТ ОХРАНЫ (Ур.1)", value=blockpost_info, inline=False)
    ### ALTAR OF FAITH
    altar_info_raw = Altar.info_list
    altar_info = "\n".join(altar_info_raw)
    info_msg.add_field(name="АЛТАРЬ ВЕРЫ (Ур.1)", value=altar_info, inline=False)
    #### PRODUCTION BUILDINGS
    ### WOOD HARVESTER
    wood_harvester_raw = WoodHarvester.info_list
    wood_harvester = "\n".join(wood_harvester_raw)
    info_msg.add_field(name="ЛЕСОРУБ (Ур.1)", value=wood_harvester, inline=False)
    ### SAWMILL
    sawmill_raw = Sawmill.info_list
    sawmill = "\n".join(sawmill_raw)
    info_msg.add_field(name="ЛЕСОПИЛКА (Ур.1)", value=sawmill, inline=False)
    ####### STONE HARVESTER
    info_text_building = StoneHarvester.info_list
    info_text_building = "\n".join(info_text_building)
    info_msg.add_field(name="КАМНЕТЁС (Ур.1)", value=info_text_building, inline=False)
    ####### IRON MINE
    info_text_building = IronMine.info_list
    info_text_building = "\n".join(info_text_building)
    info_msg.add_field(name="ЖЕЛЕЗНАЯ ШАХТА (Ур.1)", value=info_text_building, inline=False)
    ####### SILVER MINE
    info_text_building = SilverMine.info_list
    info_text_building = "\n".join(info_text_building)
    info_msg.add_field(name="СЕРЕБРЯНАЯ ШАХТА (Ур.1)", value=info_text_building, inline=False)
    ####### GOLD MINE
    info_text_building = GoldMine.info_list
    info_text_building = "\n".join(info_text_building)
    info_msg.add_field(name="ЗОЛОТАЯ ШАХТА (Ур.1)", value=info_text_building, inline=False)
    ####### RUBBIES MINE
    info_text_building = RubbiesMine.info_list
    info_text_building = "\n".join(info_text_building)
    info_msg.add_field(name="ШАХТА РУБИНОВ (Ур.1)", value=info_text_building, inline=False)
    ####### DIAMONDS MINE
    info_text_building = DiamondsMine.info_list
    info_text_building = "\n".join(info_text_building)
    info_msg.add_field(name="АЛМАЗНАЯ ШАХТА (Ур.1)", value=info_text_building, inline=False)
    ####### SMELTER
    info_text_building = Smelter.info_list
    info_text_building = "\n".join(info_text_building)
    info_msg.add_field(name="ПЛАВИЛЬНЯ (Ур.1)", value=info_text_building, inline=False)
    ####### STORAGE
    info_text_building = Storage.info_list
    info_text_building = "\n".join(info_text_building)
    info_msg.add_field(name="ГОРОДСКОЙ СКЛАД (Ур.1)", value=info_text_building, inline=False)
    ################################
    date_time = result_date[1]
    date_formatted_1 = date_time.strftime("%A %d. %B %Y")
    footer_text = f"В игре с {date_formatted_1}."
    info_msg.set_footer(text=footer_text, icon_url=bot_picture)
    #
    return info_msg


#####################################################################################################################
#####################################################################################################################
#####################################################################################################################


## Data save Utility
def _mysql_register(discord_id, guild_name, main_character_name, capital_name):

    # PROFILE_DATA
    date = str(datetime.datetime.now())
    values = (discord_id, guild_name, date, main_character_name, date, capital_name, date)
    mysql_input = f"INSERT INTO profile_data (discord_id, guild_name, guild_name_changed, main_character_name, main_character_name_changed, capital_name, capital_name_changed) VALUES {values}"
    #
    my_cursor.execute(mysql_input)
    mydb.commit()
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # INVENTORY
    value1 = discord_id
    mysql_input1 = f"INSERT INTO inventory (discord_id) VALUES ({value1})"
    #
    my_cursor.execute(mysql_input1)
    mydb.commit()
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # SKILLS
    value2 = discord_id
    mysql_input2 = f"INSERT INTO skills (discord_id) VALUES ({value2})"
    #
    my_cursor.execute(mysql_input2)
    mydb.commit()
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # DATE
    values2 = (discord_id, date)
    mysql_input3 = f"INSERT INTO date_database (discord_id, registered) VALUES {values2}"
    #
    my_cursor.execute(mysql_input3)
    mydb.commit()
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # CAPITAL_STORAGE
    value3 = discord_id
    mysql_input4 = f"INSERT INTO capital_storage (discord_id) VALUES ({value3})"
    #
    my_cursor.execute(mysql_input4)
    mydb.commit()


    return True

################################################################################

## Data update Utility
def _mysql_update_profile_data(discord_id, update_column, update_value):
    #
    if update_column == "guild_name":
        date_column = "guild_name_changed"
    elif update_column == "main_character_name":
        date_column = "main_character_name_changed"
    elif update_column == "capital_name":
        date_column = "capital_name_changed"
    else:
        raise ValueError("WRONG COLUMN TO UPDATE!")
        return False
    #
    try:
        my_cursor.execute(f"SELECT {date_column} FROM profile_data WHERE discord_id = {discord_id}")
    except Exception as e:
        print(f"'_mysql_update_profile_data' ERROR: '{e}'")
        return False
    date_changed = my_cursor.fetchall()[0][0]
    date_current = datetime.datetime.now()
    datetime_delta_changed = date_current - date_changed
    datetime_delta_standart = datetime.timedelta(hours=24)
    if datetime_delta_changed < datetime_delta_standart:
        time_left = datetime_delta_standart - datetime_delta_changed
        # MAY CAUSE SOME BUGGS # # # # # # # # # # # # # # # # # # #
        time_left = str(time_left)[:-7]  # # # # # # # # # # # # # #
        # MAY CAUSE SOME BUGGS # # # # # # # # # # # # # # # # # # #
        return f"Вы можете изменять профиль только раз в 24 часа! (Будет доступно через {time_left})"
    else:
        date = date_current
    #
    mysql_input = f"UPDATE profile_data SET {update_column} = '{update_value}' WHERE discord_id = {discord_id}"
    my_cursor.execute(mysql_input)
    mydb.commit()
    #
    mysql_input = f"UPDATE profile_data SET {date_column} = '{date}' WHERE discord_id = {discord_id}"
    my_cursor.execute(mysql_input)
    mydb.commit()
    #
    return True


################################################################################
def _construction_name(building_to_build):
    building_t = building_to_build[:-1].lower()
    building = building_to_build.lower()
    if building_t == "таверн":
        actuall_building_class = Tavern()
    elif building == "пост охраны":
        actuall_building_class = Blockpost()
    elif building == "рынок":
        actuall_building_class = Market()
    elif building == "алтарь веры":
        actuall_building_class = Altar()
    elif building == ("дровосек" or "дровосека"):
        actuall_building_class = WoodHarvester()
    elif building == ("лесопилка" or "лесопилку"):
        actuall_building_class = Sawmill()
    elif building == ("камнетёс" or "камнетёса" or "камнетес" or "камнетеса"):
        actuall_building_class = StoneHarvester()
    elif building == ("железная шахта" or "железную шахту"):
        actuall_building_class = IronMine()
    elif building == ("серебряная шахта" or "серебряную шахту"):
        actuall_building_class = SilverMine()
    elif building == ("золотая шахта" or "золотую шахту"):
        actuall_building_class = GoldMine()
    elif building == ("шахта рубинов" or "шахту рубинов"):
        actuall_building_class = RubbiesMine()
    elif building == ("алмазная шахта" or "алмазную шахту"):
        actuall_building_class = DiamondsMine()
    elif building == ("плавильня" or "плавильню"):
        actuall_building_class = Smelter()
    elif building == "городской склад":
        actuall_building_class = Storage()
    else:
        return False

    return actuall_building_class
################################################################################
def _check_if_max_buildings(building, discord_id):

    ### DATA
    my_cursor.execute(f"SELECT * FROM buildings WHERE discord_id = {discord_id} AND building_name = '{building.name}'")
    amount = len(my_cursor.fetchall())
    ###
    my_cursor.execute(f"SELECT capital_max_buildings, capital_buildings FROM profile_data WHERE discord_id = {discord_id}")
    n_max, n_cur = my_cursor.fetchall()[0]
    ###
    max_amount = building.max_amount
    #
    if amount == max_amount:
        return "Вы уже построили максимальное количество таких зданий!"
    elif n_cur == n_max:
        return f"Вы не можете построить больше зданий в вашем городе на данный момент ({n_cur}/{n_max})!"
    elif amount < max_amount and n_cur < n_max:
        return True



################################################################################
def _charge_cost(building, discord_id):

    ### DATA
    my_cursor.execute(f"SELECT money FROM profile_data WHERE discord_id = {discord_id}")
    money = my_cursor.fetchall()[0][0]
    ###
    cost = building.cost
    if cost > money:
        return "У вас в казне недостаточно денег для строительства этого здания!"
    else:
        charged = money-cost
    ### DATA
    my_cursor.execute(f"UPDATE profile_data SET money = {charged} WHERE discord_id = {discord_id}")
    mydb.commit()
    ###
    return True


################################################################################
def _set_to_construction(building, discord_id):

    ### DATA
    tmp = f"UPDATE profile_data SET is_under_construction = True WHERE discord_id = {discord_id}"
    my_cursor.execute(tmp)
    mydb.commit()
    ###
    time_of_construction = building.time_to_build
    return time_of_construction

################################################################################
def _finish_construction(building, discord_id):

    ### DATA
    values = (discord_id, building.name, building.level)
    tmp = f"INSERT INTO buildings (discord_id, building_name, level) VALUES {values}"
    my_cursor.execute(tmp)
    mydb.commit()
    ##
    tmp = f"UPDATE profile_data SET is_under_construction = False WHERE discord_id = {discord_id}"
    my_cursor.execute(tmp)
    mydb.commit()
    ##
    my_cursor.execute(f"SELECT capital_buildings FROM profile_data WHERE discord_id = {discord_id}")
    n_cur = my_cursor.fetchall()[0][0]
    n_cur += 1
    tmp = f"UPDATE profile_data SET capital_buildings = {n_cur} WHERE discord_id = {discord_id}"
    my_cursor.execute(tmp)
    mydb.commit()
    ###
    if type(building) == Storage:
        my_cursor.execute(f"SELECT storage_capacity FROM profile_data WHERE discord_id = {discord_id}")
        c_capacity = my_cursor.fetchall()[0][0]
        c_capacity += building.resource_storage
        tmp = f"UPDATE profile_data SET storage_capacity = {c_capacity} WHERE discord_id = {discord_id}"
        my_cursor.execute(tmp)
        mydb.commit()
    ###

    ###
    return f"Строительство здания '{building.name}' было успешно завершено!"


################################################################################
def _check_enough_money_lottery(discord_id, bet):

    ### DATA
    tmp = f"SELECT money FROM profile_data WHERE discord_id = {discord_id}"
    my_cursor.execute(tmp)
    money = my_cursor.fetchall()[0][0]
    ###
    if money < bet:
        return False
    elif money >= bet:
        return True

################################################################################
def _update_money_lottery(discord_id, bet, win):

    ### DATA
    tmp = f"SELECT money FROM profile_data WHERE discord_id = {discord_id}"
    my_cursor.execute(tmp)
    money = my_cursor.fetchall()[0][0]
    ### DATA

    new_money = money - bet + win

    ### DATA
    tmp = f"UPDATE profile_data SET money = {new_money} WHERE discord_id = {discord_id}"
    my_cursor.execute(tmp)
    mydb.commit()
    ### DATA
    return True

################################################################################
''' utility for lottery main chat report '''
def _get_some_info(discord_id):

    ### DATA
    tmp = f"SELECT main_character_name, guild_name FROM profile_data WHERE discord_id = {discord_id}"
    my_cursor.execute(tmp)
    info = my_cursor.fetchall()[0]
    ###
    return info

################################################################################
def _check_lvl_up(discord_id):

    ## DATA
    tmp = f"SELECT level, exp, exp_to_level, skill_points FROM skills WHERE discord_id = {discord_id}"
    my_cursor.execute(tmp)
    exp_data = my_cursor.fetchall()[0]
    level = exp_data[0]
    current_exp = exp_data[1]
    exp_to_level = exp_data[2]
    skill_points = exp_data[3]

    while current_exp >= exp_to_level:
        level += 1
        skill_points += 1
        current_exp = current_exp - exp_to_level
        exp_to_level = level * 10 + 10

        ## Update data in case of change
        tmp = f"UPDATE skills SET level = {level}, exp = {current_exp}, exp_to_level = {exp_to_level}, skill_points = {skill_points} WHERE discord_id = {discord_id}"
        my_cursor.execute(tmp)
        mydb.commit()

    return True


################################################################################
def _gain_exp(experience, discord_id):

    ## DATA
    tmp = f"SELECT exp FROM skills WHERE discord_id = {discord_id}"
    my_cursor.execute(tmp)
    exp = my_cursor.fetchall()[0][0]
    exp += experience
    ##
    ## Update exp
    tmp = f"UPDATE skills SET exp = {exp} WHERE discord_id = {discord_id}"
    my_cursor.execute(tmp)
    mydb.commit()
    ##
    _check_lvl_up(discord_id)
    #
    return True

################################################################################


def _robbery(attack_id, deff_id):
    global global_members_dic

    attack_id = str(attack_id)
    deff_id = str(deff_id)
    attacker = global_members_dic[attack_id]
    deffender = global_members_dic[deff_id]

    if attack_id == deff_id:
        return "Ты не можешь ограбить самого себя!"
    elif deff_id == "555107254819618826":
        return "Ты не можешь ограбить бота!"

    def _process():
        chance = 40
        modificator = (attacker.level - deffender.level) * 1.5
        chance += modificator
        tmp = random.randint(0, 100)
        if chance >= tmp:
            coef = attacker.robber_coef
            tmp_money = global_members_dic[deff_id]._robbered(coef)
            global_members_dic[attack_id]._robber(tmp_money)

            ############### SAVING DATA INTO TXT.FILE #######
            #_save_profiles_change() ###### IMPORTANT ########
            #################################################

            return f"Удачное ограбление, ты заработал опыт и украл {tmp_money}$!"
        else:
            global_members_dic[attack_id]._time_failed_command()
            return f"Ограбление завершилось неудачно (шанс был {chance}%)"

    if attacker._time_check_1() is True:
        if attacker._time_check_2() is True:
            return _process()
        else: return attacker._time_check_2()
    else:
        return attacker._time_check_1()
####################################################################################################


@bot.event
async def on_ready():
    global bot_channel
    global server
    global global_members_dic
    global bot_info_channel
    global global_shop
    global bot_farm_channel
    global list_of_roles

    ## print statements for DEBUGGING purposes
    server = bot.get_guild(528698800999628800)
    channels = server.channels
    #print(channels)
    bot_channel = None
    for each_channel in channels:
        if each_channel.id == 555107130617888769:
            bot_channel = each_channel
        elif each_channel.id == 570636440803999745:
            bot_info_channel = each_channel
        elif each_channel.id == 571017994730471435:
            bot_farm_channel = each_channel
    #print(f"{bot_channel}, {type(bot_channel)}")

    ## LIST OF ROLES
    list_of_roles = server.roles
    ##########
    def _delete_my_role(role_name):
        for each in list_of_roles:
            if each.name == role_name:
                return each
    ##########
    #role = _delete_my_role("PepegaLand")
    #await role.delete()
    #
    print('Bot online.')
    _logging('Bot online.')


@bot.event
async def on_member_join(member):

    await member.send("```\nИспользуйте команду '!help' чтобы посмотреть список доступных команд.```")


##
@bot.event
async def on_member_remove(member):
    global list_of_roles

    discord_id = member.id
    ###
    my_cursor.execute(f"SELECT guild_name FROM profile_data WHERE discord_id = {discord_id}")
    guild_name = my_cursor.fetchall()
    if guild_name == ():
        return
    else:
        guild_name = guild_name[0][0]
    ###
    for each_role in list_of_roles:
        if each_role.name == guild_name:
            each_role.delete()
    #
    tables = ["profile_data", "buildings", "skills", "inventory", "date_database", "capital_storage"]
    #
    for table in tables:
        tmp = f"DELETE FROM {table} WHERE discord_id = {discord_id}"
        my_cursor.execute(tmp)
        mydb.commit()

    await member.send("```\nВы покинули сервер, поэтому ваш аккаунт был удален.```")



#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
## Utilities




#######################################################################################################################
#######################################################################################################################
@bot.command(name="issue", pass_context = True)
async def _issue(ctx):
    discord_user = ctx.message.author
    discord_id = ctx.message.author.id
    show_msg = False
    ## Utility
    try:
        msg = ctx.message
        await msg.delete()
    except Exception as e:
        if str(e) != "FORBIDDEN (status code: 403): Cannot execute action on a DM channel": print(e)
    #
    my_cursor.execute(f"SELECT discord_id FROM profile_data WHERE discord_id = {discord_id}")
    result_tmp = my_cursor.fetchall()
    if result_tmp == ():
        await discord_user.send("Вы не зарегистрированы!")
        return
    ###
    try:
        raped = ctx.message.content.split()
        issue_text = " ".join(raped[1:])
        if len(raped) <= 1:
            show_msg = True
    except Exception as e:
        show_msg = True
    #
    if show_msg:
        await discord_user.send("```\nКоманда '!issue' позволяет написать разработчику о проблеме и/или баге\n"
                                "Введите: '!issue (Ваше подробное описание действий/команды в которой вы встретили баг)'```")
        return
    else:
        issue_text_moderated = f"User '{discord_user.name}' (discord_id='{discord_user.id}')\n Message:\t\"{issue_text}\""
        _write_an_issue(issue_text_moderated)
        await discord_user.send("```\nВаша проблема была записана! Спасибо, что помогаете искать недоработки и/или баги.```")
        print("User admitted a bug / an error.")



#######################################################################################################################
#######################################################################################################################
@bot.command(name="help", pass_context = True)
async def _help(ctx):
    #
    channel = ctx.message.channel
    ### SPECIAL case for users who are not in database
    my_cursor.execute(f"SELECT discord_id FROM profile_data WHERE discord_id = {discord_id}")
    result = my_cursor.fetchall()
    if result == ():
        await discord_user.send("Используйте команду '!reg' чтобы начать регистрацию. После успешного завершения регистрации вы получите доступ ко всем командам.")
        return
    ###
    commands_list_raw = ["!issue", "!reg", "!changeprof", "!я", "!лотерея"]
    commands_list = "\n".join(commands_list_raw)
    commands_list = "```\nCommands:\n{}```".format(commands_list)
    await channel.send(commands_list)

#######################################################################################################################
#######################################################################################################################
@bot.command(name="reg", pass_context = True)
async def _reg(ctx):
    discord_id = ctx.message.author.id
    discord_user = ctx.message.author
    #
    ## Utility
    try:
        msg = ctx.message
        await msg.delete()
    except Exception as e:
        if str(e) != "FORBIDDEN (status code: 403): Cannot execute action on a DM channel": print(e)
    ##
    my_cursor.execute(f"SELECT discord_id FROM profile_data WHERE discord_id = {discord_id}")
    result = my_cursor.fetchall()
    if result != ():
        await discord_user.send("Вы уже зарегистрированы!")
        return
    #
    def _create_register_embed(em_title, guild_name="", main_character_name="", capital_name=""):
        # Embed
        colour = discord.Color.dark_gold()
        #
        profile_data_list_raw = [f"Государство: {guild_name}", f"Имя персонажа: {main_character_name}", f"Название столицы: {capital_name}"]
        profile_data_list = "\n".join(profile_data_list_raw)
        profile_data_list = "**{}**".format(profile_data_list)
        info_msg = discord.Embed(description=profile_data_list, colour=colour)
        info_msg.set_author(name=em_title)
        #
        ####### ADD SOME STUFF
        #
        date_time = datetime.datetime.now()
        date_formatted_1 = date_time.strftime("%A %d. %B %Y")
        footer_text = f"Регистрация ({date_formatted_1})."
        info_msg.set_footer(text=footer_text, icon_url=bot_picture)
        #
        return info_msg


    register_info_msg = _create_register_embed("РЕГИСТРАЦИЯ ПРОФИЛЯ")
    await discord_user.send(embed=register_info_msg)
    await discord_user.send("Введите название для своего государства:")
    #
    def check(m):
        return m.author == discord_user
    #
    try:
        msg = await bot.wait_for("message", timeout=180.0, check=check)
    except asyncio.TimeoutError:
        await discord_user.send("Регистрация прервана. (Вы не отвечали длительное время)")
        return
    #
    guild_name = msg.content
    await discord_user.send("Назовите своего персонажа:")
    #
    try:
        msg = await bot.wait_for("message", timeout=180.0, check=check)
    except asyncio.TimeoutError:
        await discord_user.send("Регистрация прервана. (Вы не отвечали длительное время)")
        return
    #
    main_character_name = msg.content
    await discord_user.send("Придумайте название для своей столицы:")
    #
    try:
        msg = await bot.wait_for("message", timeout=180.0, check=check)
    except asyncio.TimeoutError:
        await discord_user.send("Регистрация прервана. (Вы не отвечали длительное время)")
        return
    #
    capital_name = msg.content
    ###
    register_info_msg = _create_register_embed("ПРОФИЛЬ", guild_name, main_character_name, capital_name)
    await discord_user.send(embed=register_info_msg)
    await discord_user.send("Подтвердите создание профиля ('ДА' если вы подтверждаете / 'НЕТ' для отмены)")
    #
    def check(m):
        def check_little():
            check_list = ["ДА", "НЕТ"]
            if m.content in check_list:
                return True
            else:
                return False
        return m.author == discord_user and check_little()
    #
    try:
        msg = await bot.wait_for("message", timeout=180.0, check=check)
    except asyncio.TimeoutError:
        await discord_user.send("Регистрация прервана. (Вы не отвечали длительное время)")
        return
    else:
        if msg.content == "НЕТ":
            await discord_user.send("Вы отменили регистрацию!")
            return
        elif msg.content == "ДА":
            pass
    # Debugging 'print'
    #print(type(discord_id), ": ", discord_id, guild_name, main_character_name, capital_name)
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    ## ADD A ROLE OF COUNTRY NAME
    member = server.get_member(discord_id)
    ### Colours
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    #
    colour = discord.Colour.from_rgb(r, g, b)
    role = await server.create_role(name=guild_name, hoist=True, colour=colour)
    await member.add_roles(role)
    #
    x = _mysql_register(discord_id, guild_name, main_character_name, capital_name)
    if not x:
        raise Exception("ERROR WHILE REGISTRATING")
    ## REPORTING TO USER
    await discord_user.send("Регистрация успешно завершена!")
    # Logging #
    _logging(f"Registration finished, d_user '{discord_user.name}' (discord_id= '{discord_id}', guild_name= '{guild_name}', main_character_name= '{main_character_name}', capital_name= '{capital_name}'")
    #
    #####
    ##### HERE CODE TO GIVE A 'PLAYER' ROLE TO THE USER AND ACCESS HIM TO THE CHATS
    #####

#######################################################################################################################
#######################################################################################################################
@bot.command(name="changeprof", pass_context = True)
async def _changeprof(ctx):
    discord_id = ctx.message.author.id
    discord_user = ctx.message.author
    return_error = False
    #
    ## Utility
    try:
        msg = ctx.message
        await msg.delete()
    except Exception as e:
        if str(e) != "FORBIDDEN (status code: 403): Cannot execute action on a DM channel": print(e)
    #
    my_cursor.execute(f"SELECT discord_id FROM profile_data WHERE discord_id = {discord_id}")
    result_tmp = my_cursor.fetchall()
    if result_tmp == ():
        await discord_user.send("Вы не зарегистрированы!")
        return
    ###
    try:
        column_to_update_raw = ctx.message.content.split()[1]
        value_to_update = " ".join(ctx.message.content.split()[2:])
    except:
        return_error = True
    #
    try:
        if column_to_update_raw == "государство":
            column_to_update = "guild_name"
        elif column_to_update_raw == "имя":
            column_to_update = "main_character_name"
        elif column_to_update_raw == "столица":
            column_to_update = "capital_name"
        else:
            return_error = True
    except:
        return_error = True

    if return_error:
        await discord_user.send("Пример использования команды '!changeprof':\n'!changeprof {что-изменить} {новое название}'\nВместо {что-изменить} используйте 'государство', 'имя', 'столица'")
    else:
        tmp = _mysql_update_profile_data(discord_id, column_to_update, value_to_update)
        if tmp == True:
            await discord_user.send("Изменения профиля успешно сохранено!")
        elif tmp != False:
            await discord_user.send(tmp)
    ##############
        _logging(f"Profile data changed, d_user {discord_user.name} (changed '{column_to_update}' with value '{value_to_update}')")
    ##############


#######################################################################################################################
#######################################################################################################################
@bot.command(name="лотерея", pass_context=True)
async def _лотерея(ctx):
    discord_id = ctx.message.author.id
    discord_user = ctx.message.author
    continue_if = True
    ## Utility
    try:
        msg = ctx.message
        await msg.delete()
    except Exception as e:
        if str(e) != "FORBIDDEN (status code: 403): Cannot execute action on a DM channel": print(e)
    #
    my_cursor.execute(f"SELECT discord_id FROM profile_data WHERE discord_id = {discord_id}")
    result_tmp = my_cursor.fetchall()
    if result_tmp == ():
        await discord_user.send("Вы не зарегистрированы!")
        return
    ###
    lottery = Lottery("Лотерея")
    ##
    try:
        bet = ctx.message.content.split()[1]
        #
    except Exception as e:
        continue_if = False
        ##### BUGS POSSIBLE #
        if str(e) != "list index out of range":
            print(e)
    #
    if continue_if:
        ## Main part
        checked_bet = lottery.check_possible_bet(bet)
        ### CHECK IF ENOUGH MONEY

        ###
        if checked_bet[0] == True:
            #
            checked_bet = checked_bet[1]
            #
            enough_money = _check_enough_money_lottery(discord_id, checked_bet)
            if enough_money == False:
                await discord_user.send("У вас в казне недостаточно денег!")
                return

            ## Main part
            image = lottery.give_image()
            _text = f"<@{discord_id}> Выберите лотерейный билет [1, 2 или 3]"
            await discord_user.send(file=image, content=_text)
            # check
            def check(m):
                nums = ["1", "2", "3"]
                return (m.content in nums) and m.author == discord_user
            #
            try:
                msg = await bot.wait_for('message', check=check, timeout=180)
            except asyncio.TimeoutError:
                await discord_user.send("Лотерея отменена. (Вы не отвечали длительное время)")
                return
            choice = int(msg.content)
            #
            money_win = lottery.play_lottery(choice, checked_bet)
            ### SAVE WIN
            saved = _update_money_lottery(discord_id, checked_bet, money_win)
            ###
            if saved:
                await discord_user.send(f"Вы выиграли {money_win}$!")
            ##
            info = _get_some_info(discord_id)
            await bot_channel.send(f"```\nОбъявление лотереи:\nГерой {info[0]} из {info[1]} сыграл в лотерею на {checked_bet}$ и получил {money_win}$!```")

        elif checked_bet[0] == False:
            bets_list = lottery.check_possible_bet(bet)[1]
            await discord_user.send(f"Для игры в лотерею введите '!лотерея (ставка)'.\nВозможные ставки: {bets_list}")
    else:
        bets_list = lottery.check_possible_bet(0)[1]
        await discord_user.send(f"Для игры в лотерею введите '!лотерея (ставка)'.\nВозможные ставки: {bets_list}")



#######################################################################################################################
#######################################################################################################################
@bot.command(name="строить", pass_context=True)
async def _строить(ctx):
    discord_id = ctx.message.author.id
    discord_user = ctx.message.author
    return_error = False
    return_menu = False
    #
    ## Utility
    try:
        msg = ctx.message
        await msg.delete()
    except Exception as e:
        if str(e) != "FORBIDDEN (status code: 403): Cannot execute action on a DM channel": print(e)
    #
    my_cursor.execute(f"SELECT discord_id FROM profile_data WHERE discord_id = {discord_id}")
    result_tmp = my_cursor.fetchall()
    if result_tmp == ():
        await discord_user.send("Вы не зарегистрированы!")
        return
    ###
    #### DATA
    my_cursor.execute(f"SELECT is_under_construction FROM profile_data WHERE discord_id = {discord_id}")
    is_under_construction = my_cursor.fetchall()[0][0]
    if is_under_construction == 0:
        is_under_construction = False
    elif is_under_construction == 1:
        is_under_construction = True
    ####
    ### Prevent double building
    if is_under_construction:
        await discord_user.send("Сейчас идет строительство и вы не можете начать новое!")
        return
    ###
    try:
        building_to_build = " ".join(ctx.message.content.split()[1:])
        all_ctx = ctx.message.content.split()[1]
        #

    except:
        return_menu = True
    ##
    if return_error:
        await discord_user.send("Используйте команду '!строить' для получения дополнительной информации")
        return
    elif return_menu:
        # Creating menu #
        menu_msg = _set_building_menu(discord_id, discord_user)
        await discord_user.send(embed=menu_msg)
        return
    else:
        #MAIN FUNCTION#
        building_to_build = _construction_name(building_to_build)
        #print(type(building_to_build))
        if building_to_build is False:
            await discord_user.send("Используйте команду '!строить' чтобы посмотреть существующие здания")
            return
        ### PREVENT unique building built twice and stuff..
        check_if_possible = _check_if_max_buildings(building_to_build, discord_id)
        if check_if_possible != True:
            await discord_user.send(check_if_possible)
            return
        ###
        ##### If enough cash - charge cost, else - return 'you're poor b***h'
        cash_check = _charge_cost(building_to_build, discord_id)
        if cash_check is not True:
            await discord_user.send(cash_check)
            return
        #####
        ###
        time_of_construction = _set_to_construction(building_to_build, discord_id)
        #print(time_of_construction)
        time = datetime.timedelta(seconds=time_of_construction)
        #print(time)
        await discord_user.send(f"Строительство начато, до конца осталось {str(time)}")
        ###
        ################# WAITING TILL CONSTRUCT
        await asyncio.sleep(time_of_construction)
        ###
        success = _finish_construction(building_to_build, discord_id)
        await discord_user.send(success)
        ##### LOGGING
        _logging(f"User '{discord_user.name}' (discord_id = '{discord_id}') HAS BUILT '{building_to_build.name}'")

#######################################################################################################################
#######################################################################################################################
@bot.command(name="улучшить", pass_context = True)
async def _улучшить(ctx):
    discord_id = ctx.message.author.id
    discord_user = ctx.message.author
    #
    ## Utility
    try:
        msg = ctx.message
        await msg.delete()
    except Exception as e:
        if str(e) != "FORBIDDEN (status code: 403): Cannot execute action on a DM channel": print(e)
    #
    my_cursor.execute(f"SELECT discord_id FROM profile_data WHERE discord_id = {discord_id}")
    result_tmp = my_cursor.fetchall()
    if result_tmp == ():
        await discord_user.send("Вы не зарегистрированы!")
        return
    #
    my_cursor.execute(f"SELECT is_under_update FROM profile_data WHERE discord_id = {discord_id}")
    result_tmp = my_cursor.fetchall()[0][0]
    if result_tmp == 1:
        await discord_user.send("Сейчас идет улучшение, вы не можете начать новое!")
        return
    #
    ##### MAIN PART
    help_txt = f"Пример команды: '!улучшить таверна'"
    try:
        building = " ".join(msg.content.split()[1:])
        building = _construction_name(building)
        if building == False:
           await discord_user.send(help_txt)
           return
    except:
           await discord_user.send(help_txt)
           return
    ### DATA
    tmp = f"SELECT building_name, level, unique_index FROM buildings WHERE discord_id = {discord_id} AND building_name = '{building.name}'"
    my_cursor.execute( tmp )
    buildings_data = my_cursor.fetchall()
    if buildings_data == ():
        await discord_user.send(f"У вас нету здания '{building.name}', которое можно было бы улучшить!")
        return
    ##
    update_embed = _set_update_embed_(discord_id, discord_user, buildings_data, building)
    #
    await discord_user.send(embed=update_embed)
    # check
    def check(m):
        return m.author == discord_user
    #
    msg = await bot.wait_for('message', check=check)
    #
    try:
        await msg.delete()
    except Exception as e:
        if str(e) != "FORBIDDEN (status code: 403): Cannot execute action on a DM channel": print(e)
    #
    try:
        level_to_update = int(msg.content.split()[0])
    except Exception as e:
        await discord_user.send("Вы ввели неверный уровень существующего здания!")
        return
        print(e)
    #
    return_fail = True
    for data in buildings_data:
        lvl_building = data[1]
        id_building = data[2]
        #
        if level_to_update == lvl_building:
            return_fail = False
    #
    if return_fail:
        await discord_user.send("Вы ввели неверный уровень существующего здания!")
        return
    #
    ########################################
    def _get_this_lvl_stats(building, lvl):
        if issubclass(type(building), Building):
            if lvl == 2:
                building._get_lvl_2
            elif lvl == 3:
                building._get_lvl_3
            elif lvl == 4:
                building._get_lvl_4
            elif lvl == 5:
                building._get_lvl_5
        else:
            if lvl != 1:
                building.get_level(lvl)
            else:
                return building
            #
        return building
    ########################################
    building = _get_this_lvl_stats(building, lvl_building+1)
    update_price = building.cost
    def _check_enough_money():
        ### DATA
        tmp = f"SELECT money FROM profile_data WHERE discord_id = {discord_id}"
        my_cursor.execute( tmp )
        money = my_cursor.fetchall()[0][0]
        ###
        if money >= update_price:
            new_money = money - update_price
            #
            ### UPDATE MONEY
            mysql_input = f"UPDATE profile_data SET money = {new_money} WHERE discord_id = {discord_id}"
            my_cursor.execute(mysql_input)
            mydb.commit()
            return True
        else:
            return False
    #
    x = _check_enough_money()
    if not x:
        await discord_user.send("У вас в казне недостаточно денег для улучшения!")
        return
    # update start
    time = building.time_to_build
    update_time = datetime.timedelta(seconds=time)
    ####
    def set_to_update():
        ### UPDATE
        mysql_input = f"UPDATE profile_data SET is_under_update = 1 WHERE discord_id = {discord_id}"
        my_cursor.execute(mysql_input)
        mydb.commit()
        return True
    ####
    set_to_update()
    await discord_user.send(f"Улучшение начато, до конца осталось {update_time}.")
    #
    await asyncio.sleep(time)
    #
    def update():
        ### UPDATE
        mysql_input = f"UPDATE profile_data SET is_under_update = 0 WHERE discord_id = {discord_id}"
        my_cursor.execute(mysql_input)
        mydb.commit()
        ###
        mysql_input = f"UPDATE buildings SET level = {lvl_building+1} WHERE unique_index = {id_building}"
        my_cursor.execute(mysql_input)
        mydb.commit()
        ##
        return True
    #
    y = update()
    if y:
        await discord_user.send(f"Здание '{building.name}' было улучшено до уровня {lvl_building+1}!")
        _logging(f"Building  '{building.name}' was updated to lvl {lvl_building+1} by {discord_user.name} (id='{discord_id}')")



#######################################################################################################################
#######################################################################################################################
@bot.command(name="город", pass_context=True)
async def _город(ctx):
    discord_id = ctx.message.author.id
    discord_user = ctx.message.author
    #
    ## Utility
    try:
        msg = ctx.message
        await msg.delete()
    except Exception as e:
        if str(e) != "FORBIDDEN (status code: 403): Cannot execute action on a DM channel": print(e)
    #
    my_cursor.execute(f"SELECT discord_id FROM profile_data WHERE discord_id = {discord_id}")
    result_tmp = my_cursor.fetchall()
    if result_tmp == ():
        await discord_user.send("Вы не зарегистрированы!")
        return
    #
    ##### MAIN PART
    embed_msg = _set_capital_embed(discord_id, discord_user)
    await discord_user.send(embed=embed_msg)
    ###


#######################################################################################################################
#######################################################################################################################
@bot.command(name="таверна", pass_context=True)
async def _таверна(ctx):
    discord_id = ctx.message.author.id
    discord_user = ctx.message.author
    #
    ## Utility
    try:
        msg = ctx.message
        await msg.delete()
    except Exception as e:
        if str(e) != "FORBIDDEN (status code: 403): Cannot execute action on a DM channel": print(e)
    #
    my_cursor.execute(f"SELECT discord_id FROM profile_data WHERE discord_id = {discord_id}")
    result_tmp = my_cursor.fetchall()
    if result_tmp == ():
        await discord_user.send("Вы не зарегистрированы!")
        return
    #
    my_cursor.execute(f"SELECT * FROM buildings WHERE discord_id = {discord_id} AND building_name = 'Таверна'")
    result_tmp = my_cursor.fetchall()
    if result_tmp == ():
        await discord_user.send("Сначала постройте таверну!")
        return
    ##### MAIN PART
    text = Tavern().spies_repr()
    await discord_user.send(f"**Tavern:**\n{text}")


#######################################################################################################################
#######################################################################################################################
@bot.command(name="склад", pass_context=True)
async def _склад(ctx):
    discord_id = ctx.message.author.id
    discord_user = ctx.message.author
    #
    ## Utility
    try:
        msg = ctx.message
        await msg.delete()
    except Exception as e:
        if str(e) != "FORBIDDEN (status code: 403): Cannot execute action on a DM channel": print(e)
    #
    my_cursor.execute(f"SELECT discord_id FROM profile_data WHERE discord_id = {discord_id}")
    result_tmp = my_cursor.fetchall()
    if result_tmp == ():
        await discord_user.send("Вы не зарегистрированы!")
        return

    ### SET storage embed
    storage_embed = _set_storage_embed(discord_id, discord_user)
    await discord_user.send(embed=storage_embed)
    ##


#######################################################################################################################
#######################################################################################################################

def _check_channel(ctx):
    channel = ctx.message.channel

    if channel==bot_channel:
        return True
    else:
        return "You're not allowed to use bot in this channel! (c) Odmin"


#######################################################################################################################
def _bibameasuring(floor, top):
    measure_done = False

    while not measure_done:
        x = random.randrange(0, 100)

        if x <= floor:
            floor-=4
            continue
        elif x >= top:
            top+=4
            continue
        else:
            measure_done = True
    return x

@bot.command(name="bibametr", pass_context=True)
async def _bibametr(ctx):
    #_logging(f"'_bibametr' command was used by '{ctx.message.author.name}' \\\\")

    try:
        channel = ctx.message.channel
        checked = _check_channel(ctx)
        if checked:
            tmp_author_name = ctx.message.author.name
            tmp_sized = _bibameasuring(15, 25)
            result_text = "У {name} биба {size} см!".format(name=tmp_author_name, size=tmp_sized)
            await bot_channel.send(result_text)
        else:
            await channel.send(checked)

        #_logging(f"Action's finished succesfuly.")
    except Exception as e:
        print(e)
        _logging(f"Action '!bibametr' got an ERROR({e}).")

#######################################################################################################################


#######################################################################################################################
@bot.command(name="mood", pass_context=True)
async def _mood(ctx):
    #_logging(f"'_mood' command was used by '{ctx.message.author.name}' \\\\")

    mood_heroes_dic = {
        "Мафиозник": img_mafiosnik_path,
        "Олд": img_old_path,
        "Пооовар": img_pooovar_path,
        "Gloria 'Opsie' Borger": img_gloria_borger_path,
        "Momo": img_momo_path,
        "Elon Musket": img_elon_musket_path,
        "Elon Musk": img_elon_musk_path,
        "Дудец": img_dudec_path,
        "Антон (СЕКС)": img_anton_path,
        "Уставший Алексеенко":img_ystavwii_alexeenko_path,

    }

    channel = ctx.message.channel
    author_name = ctx.message.author.name
    author_id = ctx.message.author.id
    checked = _check_channel(ctx)
    choice = random.choice(list(mood_heroes_dic.keys()))
    right_path = mood_heroes_dic[choice]
    file_to_upload = discord.File(fp=right_path)


    try:
        if checked:
            await bot_channel.send(f"**Ну что, проверим какой ты сегодня, <@{author_id}>**")
            await asyncio.sleep(2)
            tmp_txt = f"<@{author_id}>"
            await bot_channel.send(f"**Проверяю историю браузера {tmp_txt}...**")
            await asyncio.sleep(2)
            await bot_channel.send("**Ого..**")
            tmp_result = f"**Да ты {choice}!**"
            await bot_channel.send(file=file_to_upload, content=tmp_result)

        else:
            await channel.send(checked)

        #_logging(f"Action's finished succesfuly.")
    except Exception as e:
        print(e)
        _logging(f"Action '!mood' got an ERROR({e}).")
#######################################################################################################################

##   Robbery command ##
@bot.command(name="ограбить", pass_context=True)
async def _ограбить(ctx):
    continue_if = True
    try:
        enemy_id = ctx.message.content.split()
        #print(enemy_id)
        enemy_id = enemy_id[1].strip(">").strip("<").strip("@").strip("!")
        #print(enemy_id)
        enemy_id = int(enemy_id)
    except:
        continue_if = False

    my_id = ctx.message.author.id

    #
    tmp_channel = ctx.message.channel
    if tmp_channel != bot_channel:
        await tmp_channel.send(f"<@{my_id}> Ограбить игрока можно только в подворотне Города!")
        return
    #

    if continue_if:
        result = _robbery(my_id, enemy_id)
        await bot_channel.send(f"<@{my_id}> {result}")
    else:
        await bot_channel.send(f"<@{my_id}> Пример команды: '!ограбить <@555107254819618826>'")
## ##
#######################################################################################################################

##    kinda Roulette command ##
@bot.command(name="рулетка", pass_context=True)
async def _рулетка(ctx):
    global global_members_dic
    continue_if = True
    allowed_bets = ["10", "20", "50", "100", "200", "500"]
    my_id = ctx.message.author.id
    #
    tmp_channel = ctx.message.channel
    if tmp_channel != bot_channel:
        await tmp_channel.send(f"<@{my_id}> Поиграть в лотерею можно только у Барыги в Городе!")
        return
    #

    try:
        bet = ctx.message.content.split()[1]
        if bet in allowed_bets:
            if global_members_dic[str(my_id)]._bet_check(int(bet)) is True:
                pass
            else:
                not_allowed = global_members_dic[str(my_id)]._bet_check(int(bet))
                await bot_channel.send(not_allowed)
                return
        else:
            continue_if = False
    except Exception as e:
        continue_if = False
        ##### BUGS POSSIBLE #
        if str(e) != "list index out of range":
            print(e)

    msg_author = ctx.message.author
    if continue_if:
        ### MAIN CODE ###
        lottery_img = discord.File(fp=img_lottery_path)
        _text = f"<@{my_id}> Выберите лотерейный билет [1, 2 или 3]"
        await bot_channel.send(file=lottery_img, content=_text)
        #check
        def check(m):
            nums = ["1", "2", "3"]
            return (m.content in nums) and m.author == msg_author
        #
        msg = await bot.wait_for('message', check=check)
        #
        ### DEBUGGING
        #print(msg.content, " Type:", type(msg.content))
        #return
        #
        answer = msg.content
        #####
        casino_ticket = Roulette("Casino 777")
        finished = casino_ticket.play_roulette(global_members_dic[str(my_id)], bet, answer)
        await bot_channel.send(finished)

        ############### SAVING DATA INTO TXT.FILE #######
        #_save_profiles_change()  ###### IMPORTANT ########
        #################################################

    else:
        str_list = "$, ".join(allowed_bets)
        await bot_channel.send(f"<@{my_id}> Пример команды: '!лотерея 10'\nВозможны только фиксированые ставки: {str_list}$.")
#######################################################################################################################

## inventory command
@bot.command(name="инвентарь", pass_context=True)
async def _инвентарь(ctx):
    my_id = ctx.message.author.id
    discord_user = ctx.message.author
    discord_channel = ctx.message.channel
    ## Utility
    try:
        msg = ctx.message
        await msg.delete()
    except Exception as e:
        if str(e) != "FORBIDDEN (status code: 403): Cannot execute action on a DM channel": print(e)
    #
    my_cursor.execute(f"SELECT discord_id FROM profile_data WHERE discord_id = {my_id}")
    result_tmp = my_cursor.fetchall()
    if result_tmp == ():
        await discord_user.send("Вы не зарегистрированы!")
        return
    ###
    # Embed created
    embed_msg = _set_inventory_embed(str(my_id))
    # Embed sended
    await discord_user.send(embed=embed_msg)

#######################################################################################################################

## farm commands
@bot.command(name="фармить", pass_context=True)
async def _фармить(ctx):
    global global_members_dic
    my_id = str(ctx.message.author.id)
    #
    tmp_channel = ctx.message.channel
    if tmp_channel != bot_farm_channel:
        await tmp_channel.send(f"<@{my_id}> Вы можете фармить только в Диком лесу!")
        return
    #
    unit = global_members_dic[my_id]
    x = global_members_dic[my_id]._add_items("останки мобов")
    # SAVE PROGRESS
    #_save_profiles_change()
    #

    result = f"<@{unit.id}>  Ты получил останки мобов ({x} шт.)!"
    await bot_farm_channel.send(result)

## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
@bot.command(name="свежевать", pass_context=True)
async def _свежевать(ctx):
    global global_members_dic
    my_id = str(ctx.message.author.id)
    #
    tmp_channel = ctx.message.channel
    if tmp_channel != bot_farm_channel:
        await tmp_channel.send(f"<@{my_id}> Вы можете свежевать только в Диком лесу!")
        return
    #
    x = global_members_dic[my_id]._add_items("шкуры")
    # SAVE PROGRESS
    #_save_profiles_change()
    #

    result = f"<@{unit.id}> Ты получил шкуры ({x} шт.)!"
    await bot_farm_channel.send(result)

## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
@bot.command(name="собирать", pass_context=True)
async def _собирать(ctx):
    global global_members_dic
    my_id = str(ctx.message.author.id)
    #
    tmp_channel = ctx.message.channel
    if tmp_channel != bot_farm_channel:
        await tmp_channel.send(f"<@{my_id}> Вы можете собирать только в Диком лесу!")
        return
    #
    x = global_members_dic[my_id]._add_items("грибы")
    # SAVE PROGRESS
    #_save_profiles_change()
    #

    result = f"<@{unit.id}> Ты получил грибы ({x} шт.)!"
    await bot_farm_channel.send(result)
#######################################################################################################################


#######################################################################################################################

## taking quest command
@bot.command(name="квест", pass_context=True)
async def _квест(ctx):
    global global_members_dic
    global global_shop
    my_id = str(ctx.message.author.id)
    #
    tmp_channel = ctx.message.channel
    if tmp_channel != bot_channel:
        await tmp_channel.send(f"<@{my_id}> Вы можете брать квест только в Городе!")
        return
    #
    me = global_members_dic[my_id]
    if me._my_quest() is None:
        global_shop._take_daily_quest(me)
        result = me._my_quest()
    else:
        result = me._my_quest()
    #
    await bot_channel.send(f"**Барыга:** <@{my_id}> {result}")

## claiming quest command
@bot.command(name="сдать", pass_context=True)
async def _сдать(ctx):
    global global_members_dic
    global global_shop

    my_id = str(ctx.message.author.id)
    me = global_members_dic[my_id]
    #
    tmp_channel = ctx.message.channel
    if tmp_channel != bot_channel:
        await tmp_channel.send(f"<@{my_id}> Вы можете сдать квест только в Городе!")
        return
    #

    if me._my_quest() is None:
        result = "Сначала тебе нужно взять какой-нибудь квест!"
    else:
        result = global_shop._finish_daily_quest(me)

    await bot_channel.send(f"<@{my_id}> {result}")


#######################################################################################################################



#######################################################################################################################
##   CLEARING FUNCTION   ##
@commands.has_role('Крысъ')
@bot.command(name="clear", pass_context=True)
async def _clear(ctx):
    #msg = ctx.message
    chosen_channel = ctx.message.channel
    #
    logs = await chosen_channel.history(limit=100).flatten()
    for each_message in logs:
        if each_message.pinned == True:
            logs.remove(each_message)
    await chosen_channel.delete_messages(logs)
#######################################################################################################################


#######################################################################################################################
## INITIALIZING MSG ##
@commands.has_role('Крысъ')
@bot.command(name="init", pass_context=True)
async def _init(ctx):

    msg = ctx.message
    async def _clear_mod():
        logs = await bot_info_channel.history(limit=100).flatten()
        await bot_info_channel.delete_messages(logs)

    await _clear_mod()

    # Creating info msg (EMBED)
    colour = discord.Color.dark_gold()
    em_content = ''' **Народ, пропонуйте свої ідеї по функціоналу бота (в лс <@314444768874594305>)**\n P.S. **Бот працює в тестовому режимі: профілі час від часу обнуляються**'''
    info_msg = discord.Embed(description=em_content, colour=colour)
    info_msg.set_author(name="ІНФО")
    command_list_raw = ["!reg - команда для регистрации", "!changeprof", "!я", "!лотерея {сумма}", "!issue"] #, "!баланс", "!инвентарь"
                        #"!bibametr", "!mood", "!ограбить {жертва}",
                        #"!фармить", "!собирать", "!свежевать", "!квест", "!сдать"]
    command_list = "\n".join(command_list_raw)
    command_list = "**{}**".format(command_list)
    info_msg.add_field(name="Команди", value=command_list, inline=False)

    ### ODD info
    odd_info = f"Ідеї, які розробляються:\nGLOBAL patch 0.1"
    info_msg.add_field(name="В процесі розробки", value=odd_info, inline=False)

    ### VERSION footer
    info_msg.set_footer(text=bot_version, icon_url=bot_picture)
    tmp_msg_sent = await bot_info_channel.send(embed=info_msg)

    ## Pin/Clearing
    await tmp_msg_sent.pin()
    try:
        await bot_info_channel.send("Clearing chat..")
        logs = await bot_info_channel.history(limit=100).flatten()
        for each_message in logs:
            if each_message.pinned == True:
                logs.remove(each_message)
        await bot_info_channel.delete_messages(logs)
    except:
        print("~~ ERROR in Pin/Clearing! ~~")
#######################################################################################################################
#######################################################################################################################



#######################################################################################################################
@commands.has_role('Крысъ')
@bot.command(name="show_profiles", pass_context=True)
async def _show_profiles(ctx):
    members = server.members
    for _ in range(len(members)):
        i = str(members[_].id)
        await bot_channel.send(global_members_dic[i])

    #global_members_list = [Profile(member) for member in members]
    # Debugg
    #print([each for each in global_members_list])

#######################################################################################################################
@bot.command(name="я", pass_context=True)
async def _я(ctx):
    discord_id = ctx.message.author.id
    discord_user = ctx.message.author
    discord_channel = ctx.message.channel
    ## Utility
    try:
        msg = ctx.message
        await msg.delete()
    except Exception as e:
        if str(e) != "FORBIDDEN (status code: 403): Cannot execute action on a DM channel": print(e)
    #
    my_cursor.execute(f"SELECT discord_id FROM profile_data WHERE discord_id = {discord_id}")
    result_tmp = my_cursor.fetchall()
    if result_tmp == ():
        await discord_user.send("Вы не зарегистрированы!")
        return
    ###
    # Embed created
    embed_msg = _set_profile_embed(discord_id, discord_user)
    # Embed sended
    await discord_user.send(embed=embed_msg)

@bot.command(name="баланс", pass_context=True)
async def _баланс(ctx):
    my_id = str(ctx.message.author.id)
    cash = global_members_dic[my_id].money
    _text = f"<@{my_id}> Ваш баланс: {cash}$"
    tmp_channel = ctx.message.channel
    await tmp_channel.send(_text)
#######################################################################################################################
#######################################################################################################################


#@commands.has_role('Крысъ')
@bot.command(name="exp", pass_context=True)
async def _exp(ctx):

    discord_id = ctx.message.author.id
    discord_user = ctx.message.author
    ##
    try:
        exp = int(ctx.message.content.split()[1])
    except Exception as e:
        print(e)
    ##
    x =_gain_exp(exp, discord_id)
    ##
    if x: await discord_user.send(f"Ты получил опыт! ({exp})")
    else: pass



#######################################################################################################################

bot.loop.create_task(connect_to_mysql())
bot.loop.create_task(calculate_every_hour())
bot.run(TOKEN)