''' XML, библиотека ElementTree, библиотека lxml '''

# https://pep8.ru/doc/dive-into-python-3/14.html

# example1.xml

# xml element:
#  <tag id="1">содержимое тега, текст, элемент</tag>
#  <tag/>
# id - атрибут

# представление данных в виде деревьев

# from xml.etree import ElementTree

# tree = ElementTree.parse('example1.xml')
# root = tree.getroot()

# use root = ElementTree.fromstring(string_xml_data) to parse from str

# print(root) # <Element 'studentsList' at 0x0000018CEA7B3F60>
# print(root.tag, root.attrib) # studentsList {}

# for child in root:
#     print(child.tag, child.attrib)
# student {'id': '1'}
# student {'id': '2'}

# print(root[0][0].text) # Greg

# for element in root.iter('scores'):
#     print(element)
# <Element 'scores' at 0x0000018CEA811350>
# <Element 'scores' at 0x0000018CEA811030>

# for element in root.iter('scores'):
#     score_sum = 0
#     for child in element:
#         score_sum += float(child.text)
#     print(score_sum) # 240.0 240.2

# tree.write('example_copy.xml')

# greg = root[0]
# module1 = next(greg.iter('module1'))
# print(module1, module1.text) # <Element 'module1' at 0x0000018CEA811A80> 70
# module1.text = str(float(module1.text) + 30)

# tree.write('example_modified.xml')

# from xml.etree import ElementTree

# tree = ElementTree.parse('example_modified.xml')
# root = tree.getroot()
# # увеличили баллы грегу => можем поменять сертификат
# greg = root[0]

# certificate = greg[2]
# certificate.set('type', 'with distinction')

# tree.write('example_modified.xml')
# <certificate type="with distinction">True</certificate>

# добавление нового элемента
# description =  ElementTree.Element('description')
# description.text = 'Showed excellent skills during the course'
# greg.append(description)
# <description>Showed excellent skills during the course</description>

# удаление элемента
# description = greg.find('description') # ищет первый элемент
# greg.remove(description)

# tree.write('example_modified.xml')

# CREATING A TREE FROM SCRATCH
# root = ElementTree.Element("student")

# first_name = ElementTree.SubElement(root, "firstName")
# first_name.text = "Greg"
# second_name = ElementTree.SubElement(root, "secondName")
# second_name.text = "Dean"

# scores = ElementTree.SubElement(root, "scores")
# module1 = ElementTree.SubElement(scores, "module1")
# module1.text = "100"
# module2 = ElementTree.SubElement(scores, "module2")
# module2.text = "80"
# module3 = ElementTree.SubElement(scores, "module3")
# module3.text = "90"

# tree = ElementTree.ElementTree(root)
# tree.write("WrittneTree.xml")

# from xml.etree import ElementTree

# from lxml import etree
# import requests

# res = requests.get('https://docs.python.org/3/')
# print(res.status_code)
# print(res.headers['Content-Type'])

# parser = etree.HTMLParser()
# root = etree.fromstring(res.text, parser)

# for element in root.iter('a'):
#     print(element, element.attrib)

''' Задание '''

# Вам дано описание пирамиды из кубиков в формате XML.
# Кубики могут быть трех цветов: красный (red), зеленый (green) и синий (blue).
# Для каждого кубика известны его цвет, и известны кубики, расположенные прямо 
# под ним.

# Пример:

# <cube color="blue">
#   <cube color="red">
#     <cube color="green">
#     </cube>
#   </cube>
#   <cube color="red">
#   </cube>
# </cube>
 
# Введем понятие ценности для кубиков. Самый верхний кубик, соответствующий 
# корню XML документа имеет ценность 1. Кубики, расположенные прямо под ним, 
# имеют ценность 2. Кубики, расположенные прямо под нижележащими кубиками, 
# имеют ценность 3. И т. д.

# Ценность цвета равна сумме ценностей всех кубиков этого цвета.

# Выведите через пробел три числа: ценности красного, зеленого и синего цветов.


# from xml.etree.ElementTree import XMLParser
# exampleXml = input()

# colors = [0, 0, 0]

# class MaxDepth:                     # The target object of the parser
#     maxDepth = 0
#     depth = 0
#     def start(self, tag, attrib):   # Called for each opening tag.
#         self.depth += 1

#         if attrib['color'] == 'red':
#             colors[0] += self.depth
#         elif attrib['color'] == 'green':
#             colors[1] += self.depth
#         elif attrib['color'] == 'blue':
#             colors[2] += self.depth
#         else:
#             pass

#         if self.depth > self.maxDepth:
#             self.maxDepth = self.depth
#     def end(self, tag):             # Called for each closing tag.
#         self.depth -= 1
#     def data(self, data):
#         pass            # We do not need to do anything with data.
#     def close(self):    # Called when all data has been parsed.
#         return self.maxDepth

# target = MaxDepth()
# parser = XMLParser(target=target)
# parser.feed(exampleXml)
# parser.close()
# print(*colors)


###  Другие решения

# from xml.etree import ElementTree

# root = ElementTree.fromstring(input())
# colors = {"red": 0, "green": 0, "blue": 0}

# def getcubes(root, value):
#     colors[root.attrib['color']] += value
#     for child in root:
#         getcubes(child, value+1)

# getcubes(root,1)
# print(colors["red"], colors["green"], colors["blue"])

### 


