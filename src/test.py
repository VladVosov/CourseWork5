import src.getting_data
import src.saving_data


test = src.getting_data.GD_on_API('', 15478)
test = test.get_request().json()
test2 = src.saving_data.Saving(test)
test2.add_vacancy()
test3 = test2.get_vacancy(1)
print(test3)
test2.del_vacancy()