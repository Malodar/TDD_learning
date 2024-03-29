# -*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import unittest


class NewVisitorTest(unittest.TestCase):
    """Тест нового посетителя"""

    def setUp(self):
        self.browser = webdriver.Firefox(executable_path='/home/artsiom/geckodriver')
        self.browser.wait = WebDriverWait(self.browser, 15)

    def tearDown(self):
        """демонтаж"""
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        """Подтверждение строки в таблице списка"""
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        """тест: можно начать список и получить его позже"""

        """Эдит слышала про крутое новое онлайн-приложение со списком неотложных дел.
        Она решает оценить его домашнюю страницу"""
        self.browser.get('http://localhost:8000')

        """Она видит, что заголовок и шапка страницы говорят о списках неотложных дел"""
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        """Ей сразу же предлагается ввести элемент списка"""
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        """Она набирает в текстовом поле "купить павлиньи перья" (ее хобби - 
        вязание рыболовных мушек)"""
        inputbox.send_keys('купить павлиньи перья')

        """Когда она нажимает Enter, страница обновляется, и теперь страница содержит 
        "1: Купить павлиньи перья" в качестве элемента списка"""
        inputbox.send_keys(Keys.ENTER)
        self.browser.wait.until(EC.presence_of_all_elements_located)
        sleep(1.2)

        self.check_for_row_in_list_table('1: купить павлиньи перья')

        """Текстовое поле по-прежнему приглашает ее добавить еще один элемент.
        Она вводит "Сделать мушку из павлиньих перьев" (Эдит очень методична)"""
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Сделать мушку из павлиньих перьев')
        inputbox.send_keys(Keys.ENTER)
        self.browser.wait.until(EC.presence_of_all_elements_located)
        sleep(1.2)



        """Страница снова обновляется, и теперь показывает оба элемента ее списка"""
        self.check_for_row_in_list_table('1: купить павлиньи перья')
        self.check_for_row_in_list_table('2: Сделать мушку из павлиньих перьев')

        """Эдит интересно, запомнит ли сайт ее список. Далее она видит, что
        сайт сгенерировал для нее уникальный URL-адрес -- об этом выводится небольшой текст 
        с обьяснениями"""
        self.fail('Закончить тест!')
        """Она посещает этот URL-адрес -- ее список по-прежнему там."""

        """Удовлетворенная, она снова ложится спать"""


if __name__ == '__main__':
    unittest.main(warnings='ignore')
