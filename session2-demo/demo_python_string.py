# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.3
#   kernelspec:
#     display_name: .venv
#     language: python
#     name: python3
# ---

# %% [markdown] id="7e2c9792"
# # Demo giới thiệu Python String

# %% [markdown] id="b712bc6f"
# ## Khai báo cơ bản

# %% id="e38ee481" outputId="8fbdf421-21bc-4567-a8df-41b3a9c6ab68" colab={"base_uri": "https://localhost:8080/"}
print("Hello world")
print('Hello world')

# %% [markdown] id="db1b1304"
# ## Lồng dấu nháy

# %% id="806f27c1" outputId="755cc53a-2a01-4b81-f279-263e15a1ad47" colab={"base_uri": "https://localhost:8080/"}
print("It's alright")
print('He is "John"')

# %% [markdown] id="eecaacf3"
# ## Gán vào biến

# %% id="7cce1e9b" outputId="3716f6a8-d71b-4ccd-d1eb-63769c54b168" colab={"base_uri": "https://localhost:8080/"}
a = "Hello"
print(a)

# %% [markdown] id="21d02208"
# ## Chuỗi nhiều dòng

# %% id="8b6c85c9" outputId="54b4b430-0881-4d69-e8e1-80fa9e8f307d" colab={"base_uri": "https://localhost:8080/"}
a = """Lorem
ipsum
dolor"""

print(a)

# %% [markdown] id="6d6fd6c9"
# ## Kiểm tra tính bất biến

# %% id="bdecaf66"
immute = "Python"
immute[0] = C

# %% [markdown] id="30d7d798"
# ## Slicing chuỗi

# %% id="43cf0dfa" outputId="bda7e6e3-8d11-450c-e0db-d55ed5472f83" colab={"base_uri": "https://localhost:8080/"}
slicing = "Hello,''World!"
print("Độ dài chuỗi:",len(slicing))
print("Output của slicing[2:5]:", slicing[2:5])
print("Output của slicing[:5]:", slicing[:5])
print("Output của slicing[2:]:", slicing[2:])
print("Output của slicing[-5:-2]:" ,slicing[-5:-2])

# %% [markdown] id="0c29ace4"
# ## Biến đổi chuỗi

# %% id="e551ef8e" outputId="c80febcd-e1f2-4c4d-ea8d-0f489170b976" colab={"base_uri": "https://localhost:8080/"}
a = "Hello, World!"
b = "xxHello Worldxx"
print("String gốc a:", a)
print("String gốc b:", b)
print("Sau khi dùng a.upper()", a.upper())
print("Sau khi dùng a.lower()", a.lower())
print("Sau khi dùng b.strip()", b.strip("xx"))
print("Sau khi dùng a.replace()", a.replace("H", "J"))
print("Sau khi dùng a.split()", a.split(","))

# %% [markdown] id="0387f2fb"
# ## Nối chuỗi

# %% id="89f2d41f" outputId="e8767d0d-75dd-4b5e-946c-9719ac167ce8" colab={"base_uri": "https://localhost:8080/"}
a = "Hello"
b = "World"
print("a + b =", a + b)
print("Thêm khoảng trắng a + ' ' + b =", a + ' ' + b)

# %% [markdown] id="820d2e4c"
# ## F-string

# %% id="fb08feb2" outputId="eaea161a-3164-4650-d23e-fde18054450c" colab={"base_uri": "https://localhost:8080/"}
name = "John"
age = 36
price = 59
print(f"Chèn biến trực tiếp: My name is {name}, I am {age} years old")
print(f"Định dạng số: The price is {price:.2f} dollars")
print(f"Tính toán biểu thức trực tiếp : The price is {20 * 59} dollars")

# %% [markdown] id="91e54a59"
# ## Escape Characters

# %% [markdown] id="3301dfbc"
# #### 1. Dấu nháy đơn (`\'`)

# %% id="4b07000d" outputId="f4718eb1-aaf3-4e1d-c834-e5b7c504e6ab" colab={"base_uri": "https://localhost:8080/"}
print('He\'s John')

# %% id="9XOuxJ6whb-J"

# %% [markdown] id="d2eb00ab"
# #### 2. Dấu nháy kép (`\"`)

# %% id="df2ab223" outputId="7dc8afa8-f466-4c8a-9617-c92bbf0a9561" colab={"base_uri": "https://localhost:8080/"}
json_text = "{\"name\": \"John\", \"age\": 20}"
print(json_text)

# %% [markdown] id="767e70c8"
# #### 3. Dấu gạch chéo ngược (`\\`)

# %% id="2cdecb73" outputId="023ae570-4fdf-4718-b5dd-1e597ad6fd8e" colab={"base_uri": "https://localhost:8080/"}
print("C:\\Users\\Admin\\Documents")

# %% [markdown] id="d6072b1b"
# #### 4. Xuống dòng mới (`\n`)

# %% id="9a50462d" outputId="1dbec0f3-a7ce-46af-95ef-0b313bef8788" colab={"base_uri": "https://localhost:8080/"}
print("Hello\nWorld")

# %% [markdown] id="4248ca25"
# #### 5. Tab (`\t`)

# %% id="bb67dd28" outputId="5be6f89d-dd19-4398-a961-7e258d7c0289" colab={"base_uri": "https://localhost:8080/"}
print("Name\tAge\tScore")
print("John\t20\t95")

# %% [markdown] id="30185c14"
# ## Các built-in method của chuỗi

# %% [markdown] id="2ad676e5"
# ### I. Phương thức tìm kiếm

# %% id="904aaeda" outputId="bded790f-5a6f-44cb-d409-283a1906a886" colab={"base_uri": "https://localhost:8080/"}
text = "Hello World Hello Python"
print("Chuỗi gốc:", text)
print()

# %% [markdown] id="d627a4d7"
# #### 1. `find()`

# %% id="167f144a" outputId="b1df353e-8849-45dd-bc3d-6d92979bae3e" colab={"base_uri": "https://localhost:8080/"}
print("Tìm 'Hello':", text.find("Hello"))
print("Tìm 'Python':", text.find("Python"))
print("Tìm 'Java':", text.find("Java"))
print()

# %% [markdown] id="e9e202ed"
# #### 2. `rfind()`

# %% id="1dc47316" outputId="9dec6e4a-fb1e-4c13-8ac2-ed666bab9995" colab={"base_uri": "https://localhost:8080/"}
print("Tìm 'Hello' từ phải sang trái:", text.rfind("Hello"))
print("Tìm 'Java' từ phải sang trái:", text.rfind("Java"))
print()

# %% [markdown] id="bcb5e053"
# #### 3. `index()`

# %% id="d004f758" outputId="756568a2-3322-4b05-a332-f0093da57d84" colab={"base_uri": "https://localhost:8080/"}
print("Vị trí của 'Python':", text.index("Python"))
# print(text.index("Java"))
# print("Lỗi ValueError: Không tìm thấy 'Java'")
print()

# %% [markdown] id="d1b42af5"
# #### 4. `rindex()`

# %% id="a8248faf" outputId="80606ae4-a73f-4381-ac3b-e635f4b52379" colab={"base_uri": "https://localhost:8080/"}
print("Vị trí cuối cùng của 'Hello':", text.rindex("Hello"))
# print(text.rindex("Java"))
# print("Lỗi ValueError: Không tìm thấy 'Java'")
print()

# %% [markdown] id="893d7fbd"
# #### 5. `count()`

# %% id="e7faad46" outputId="89c9e2e4-2229-412f-a00d-e2cd85246faa" colab={"base_uri": "https://localhost:8080/"}
print("Số lần xuất hiện của 'Hello':", text.count("Hello"))
print("Số lần xuất hiện của 'o':", text.count("o"))
print()

# %% [markdown] id="411b24d6"
# #### 6. `startswith()`

# %% id="db32e8c0" outputId="65ee4180-11f9-41d4-9945-2cbabd9fb7d3" colab={"base_uri": "https://localhost:8080/"}
print("Bắt đầu bằng 'Hello':", text.startswith("Hello"))
print("Bắt đầu bằng 'Python':", text.startswith("Python"))
print()

# %% [markdown] id="0cafea39"
# #### 7. `endswith()`

# %% id="1995afef" outputId="3e790ce3-e48e-4bac-d12f-0fbc2fc932ee" colab={"base_uri": "https://localhost:8080/"}
print("Kết thúc bằng 'Python':", text.endswith("Python"))
print("Kết thúc bằng 'Hello':", text.endswith("Hello"))
print()

# %% [markdown] id="62261e82"
# ### II. Phương thức kiểm tra

# %% [markdown] id="3f70eeb1"
# #### 1. `isalnum()`

# %% id="44279487" outputId="00f43b04-9933-4a44-ecb4-b255e548d181" colab={"base_uri": "https://localhost:8080/"}
print("'Python123'.isalnum() =", "Python123".isalnum())
print("'Python 123'.isalnum() =", "Python 123".isalnum())
print()

# %% [markdown] id="05e48dc1"
# #### 2. `isalpha()`

# %% id="6f7cdd02" outputId="bc86f37c-d515-4a66-f2b2-4c30e83ca2d2" colab={"base_uri": "https://localhost:8080/"}
print("'Python'.isalpha() =", "Python".isalpha())
print("'Python123'.isalpha() =", "Python123".isalpha())
print()

# %% [markdown] id="255f5b71"
# #### 3. `isdigit()`

# %% id="f3734dde" outputId="4a834ac6-6aee-432d-a927-5f0739ab927f" colab={"base_uri": "https://localhost:8080/"}
print("'12345'.isdigit() =", "12345".isdigit())
print("'123a'.isdigit() =", "123a".isdigit())
print()

# %% [markdown] id="301c4bd3"
# #### 4. `isdecimal()`

# %% id="b8c1c3d0" outputId="d4422173-c291-42a8-801b-56c304101398" colab={"base_uri": "https://localhost:8080/"}
print("'12345'.isdecimal() =", "12345".isdecimal())
print("'12.5'.isdecimal() =", "12.5".isdecimal())
print()

# %% [markdown] id="07050c71"
# #### 5. `isnumeric()`

# %% id="ac514aba" outputId="338fb4e7-e1f3-4e84-a5b5-955f647e29c2" colab={"base_uri": "https://localhost:8080/"}
print("'12345'.isnumeric() =", "12345".isnumeric())
print("'12.5'.isnumeric() =", "12.5".isnumeric())
print()

# %% [markdown] id="b1080065"
# #### 6. `islower()`

# %% id="79e3821e" outputId="f73b4c35-a944-4c05-c48c-1905a1979af7" colab={"base_uri": "https://localhost:8080/"}
print("'hello'.islower() =", "hello".islower())
print("'Hello'.islower() =", "Hello".islower())
print()

# %% [markdown] id="3204d2c2"
# #### 7. `isupper()`

# %% id="a4f603cf" outputId="a5baf385-9a2d-42fe-efd7-482855168821" colab={"base_uri": "https://localhost:8080/"}
print("'HELLO'.isupper() =", "HELLO".isupper())
print("'Hello'.isupper() =", "Hello".isupper())
print()

# %% [markdown] id="2db3c990"
# ### III. Biến đổi & Định dạng

# %% [markdown] id="78468a58"
# #### 1. `join()`

# %% id="8dcb03f4" outputId="3d286aa0-ab11-44d8-d36a-6eaeb165638a" colab={"base_uri": "https://localhost:8080/"}
words = ["Hello", "World", "Python"]
print("List gốc:", words)
print("' '.join(words) =", " ".join(words))
print("'-'.join(words) =", "-".join(words))
print()

# %% [markdown] id="1a1f87e8"
# #### 2. `split()`

# %% id="e3be6d17" outputId="999173cc-36c9-4974-f7af-c1c4897f690a" colab={"base_uri": "https://localhost:8080/"}
text = "Hello World Python"
print("Chuỗi gốc:", text)
print("text.split() =", text.split())
print()

# %% [markdown] id="1f0184d8"
# #### 3. `rsplit()`

# %% id="c361ca49" outputId="bae6a323-7a90-404f-a2d3-b455ceb0470b" colab={"base_uri": "https://localhost:8080/"}
text = "one,two,three,four"
print("Chuỗi gốc:", text)
print("text.rsplit(',', 1) =", text.rsplit(",", 1))
print()

# %% [markdown] id="48b0db8c"
# #### 4. `strip()`

# %% id="8935caa4" outputId="90057504-024c-4d72-a362-bb4ea4cbc586" colab={"base_uri": "https://localhost:8080/"}
text = "   Hello World   "
print("Trước strip():", repr(text))
print("Sau strip():", repr(text.strip()))
print()

# %% [markdown] id="c0e7d4bc"
# #### 5. `lstrip()`

# %% id="c4b8c780" outputId="0de4053f-0da4-4398-83b9-f21fc99085ea" colab={"base_uri": "https://localhost:8080/"}
text = "   Hello World   "
print("Trước lstrip():", repr(text))
print("Sau lstrip():", repr(text.lstrip()))
print()

# %% [markdown] id="3a01716b"
# #### 6. `replace()`

# %% id="bb8057c8" outputId="58d9f07f-342a-4593-d76d-58a8cd38688f" colab={"base_uri": "https://localhost:8080/"}
text = "Hello World"
print("Chuỗi gốc:", text)
print("text.replace('World', 'Python') =", text.replace("World", "Python"))
print()

# %% [markdown] id="6feed339"
# #### 7. `zfill()`

# %% id="e7b10db7" outputId="293f9565-3dca-4e71-92c3-03cb10a28963" colab={"base_uri": "https://localhost:8080/"}
number = "42"
print("Chuỗi gốc:", number)
print("number.zfill(5) =", number.zfill(5))
print("number.zfill(8) =", number.zfill(8))
print()

