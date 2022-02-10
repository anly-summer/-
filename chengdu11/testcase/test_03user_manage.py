
from public.pages.basepages import Basepages
from public.pages.page_element import p
from time import sleep
class user_manage(Basepages):
    @classmethod
    def setUpClass(cls) -> None:
        pass
    def tearDown(self) -> None:
        pass
    def test_user_manage(self):
        #点击用户管理
        # usermanage=["xpath","//*[@id='menu-user']/dd/ul/li[1]/a"]
        elem=Basepages.find_element(p.user_manage)
        Basepages.click(elem)
        sleep(3)
        elem1=Basepages.find_element(p.iframe)
        Basepages.switch_iframe(elem1)
        sleep(1)
    # def test_add_user(self):
        #点击添加用户
        elem2=Basepages.find_element(p.add_user)
        Basepages.click(elem2)