
# 目錄
# 1.  Digital Root
# 2.  Maximum Collatz Cycle Length
# 3.  Election Count
# 4.  Parking Fee
# 5.  Selection Sort Visualization
# 6.  Hexadecimal to Decimal
# 7.  Prefix to Infix Conversion
# 8.  Decode the Receipt
# 9.  Two Sum
# 10. GCD & LCM
# 11. Decimal to Binary
# 12. String Run-Length Encoding

# ==========================================
# 1. Digital Root
# ==========================================

import sys

# Digital Root
# 給多行正整數，每行輸出其數位根，讀到END停止
# 數位根：反覆把各位數字加總，直到剩一位數
# 數學公式：n%9==0 → 9，否則 → n%9

for line in sys.stdin:
    line = line.strip()
    if line == "END":                                  # 讀到END結束
        break
    n = int(line)
    print(9 if n % 9 == 0 else n % 9)                 # 套公式輸出

# 題目變化應對：
# 若改成其他進位的數位根 → 先轉十進位再套公式
# 若改成輸出每一步過程 → 用while迴圈逐步印出中間結果
# 若改成base b的數位根 → 公式變成 n%(b-1)==0 ? b-1 : n%(b-1)
# 若終止條件改成0或空行 → 把 "END" 換成對應條件即可

# ==========================================
# 2. Maximum Collatz Cycle Length
# ==========================================

import sys

# Maximum Collatz Cycle Length
# 給多行 i j，輸出 i j 以及 [min(i,j), max(i,j)] 中最大的 Collatz 循環長度
# Collatz規則：奇數→3N+1，偶數→N/2，直到N==1，計算步數
# 讀到 0 0 停止，輸出順序照輸入的 i j 不可對調

def collatz_length(n):
    count = 1
    while n != 1:                                      # 一直跑直到等於1
        if n % 2 == 0:                                 # 偶數除2
            n //= 2
        else:                                          # 奇數乘3加1
            n = 3 * n + 1
        count += 1
    return count

for line in sys.stdin:
    line = line.strip()
    i, j = map(int, line.split())
    if i == 0 and j == 0:                             # 讀到0 0結束
        break
    lo, hi = min(i, j), max(i, j)
    max_len = max(collatz_length(n) for n in range(lo, hi + 1))  # 找區間最大長度
    print(i, j, max_len)                               # 照原本i j順序輸出

# 題目變化應對：
# 若改成輸出最長序列的起始數字 → 記錄max_len對應的n一起輸出
# 若改成輸出完整序列 → 把while迴圈改成收集每步結果再印出
# 若範圍很大需要加速 → 用dict做記憶化(memoization)快取已算過的結果
# 若改成找最小長度 → max() 換成 min()

# ==========================================
# 3. Election Count
# ==========================================

import sys

# Election Count
# 給候選人名單，讀取選票，統計得票數，輸出贏家、最高票數、無效票數
# 不在名單內的選票算無效票，不計入任何人
# 若同票則全部列出，依字母順序排列，零票候選人仍可獲勝

lines = sys.stdin.read().splitlines()
idx = 0

n = int(lines[idx]); idx += 1                          # 讀候選人數量
candidates = []
for _ in range(n):
    candidates.append(lines[idx]); idx += 1            # 讀候選人名單

votes = {name: 0 for name in candidates}               # 初始化每人票數為0
invalid = 0

while idx < len(lines):
    ballot = lines[idx]; idx += 1
    if ballot == "END":                                # 讀到END結束
        break
    if ballot in votes:                                # 有效票加給對應候選人
        votes[ballot] += 1
    else:                                              # 不在名單內算無效票
        invalid += 1

max_votes = max(votes.values())                        # 找最高票數
winners = sorted(k for k, v in votes.items() if v == max_votes)  # 同票全列出，字母排序

print("Winner:", " ".join(winners))
print("Votes:", max_votes)
print("Invalid:", invalid)

# 題目變化應對：
# 若改成輸出所有候選人得票數 → 印出 votes 字典每個項目
# 若改成不區分大小寫 → ballot = ballot.lower() 再比對
# 若改成多輪投票制 → 外層加迴圈，每輪重置votes重新計算
# 若改成輸出得票率 → fee = votes[name] / sum(votes.values()) * 100

# ==========================================
# 4. Parking Fee
# ==========================================

import sys
import math

# Parking Fee
# 給停車場時費，讀取進出事件，計算每台車的停車費
# 不足一小時無條件進位，最少收一小時
# 未離場的車最後依進場順序列出

lines = sys.stdin.read().splitlines()
idx = 0

rate = int(lines[idx]); idx += 1                       # 讀時費

entry_time = {}                                        # 記錄每台車進場時間
entry_order = []                                       # 記錄進場順序
departed = []                                          # 記錄離場順序與費用

def to_minutes(t):                                     # 時間轉換成分鐘
    h, m = map(int, t.split(":"))
    return h * 60 + m

while idx < len(lines):
    line = lines[idx]; idx += 1
    if line == "END":                                  # 讀到END結束
        break
    parts = line.split()
    event, plate, time = parts[0], parts[1], parts[2]

    if event == "IN":                                  # 進場：記錄時間與順序
        entry_time[plate] = to_minutes(time)
        entry_order.append(plate)
    elif event == "OUT":                               # 離場：計算停留時間與費用
        duration = to_minutes(time) - entry_time[plate]
        hours = math.ceil(duration / 60)               # 不足一小時無條件進位
        hours = max(hours, 1)                          # 最少收一小時
        fee = hours * rate
        departed.append((plate, fee))
        entry_order.remove(plate)                      # 從未離場清單移除

for plate, fee in departed:                            # 依離場順序輸出費用
    print(f"{plate}: ${fee}")

if entry_order:                                        # 仍在場的車依進場順序列出
    print("Still parked:", ",".join(entry_order))

# 題目變化應對：
# 若改成按分鐘計費 → 拿掉ceil，直接 duration * rate
# 若改成跨日計算 → 時間加上日期欄位，改用datetime處理
# 若改成不同時段不同費率 → 依進場時間判斷費率區間再套用
# 若改成輸出總收入 → 累加所有fee最後印出

# ==========================================
# 5. Selection Sort Visualization
# ==========================================

import sys

# Selection Sort Visualization
# 給一串整數，模擬選擇排序，每次找未排序部分的最小值
# 每個回合輸出最小值在整體陣列的索引（非子陣列索引）
# 最後輸出排序完成的陣列

nums = list(map(int, sys.stdin.read().split()))        # 讀取整數陣列
n = len(nums)

for i in range(n - 1):                                 # 每回合從i開始找最小值
    min_idx = i
    for j in range(i + 1, n):                         # 找未排序部分的最小值索引
        if nums[j] < nums[min_idx]:
            min_idx = j
    nums[i], nums[min_idx] = nums[min_idx], nums[i]   # 最小值換到已排序末端
    print(min_idx)                                     # 輸出最小值的整體索引

print(*nums)                                           # 輸出排序後的陣列

# 題目變化應對：
# 若改成Bubble Sort → 外層i，內層j從0到n-i-1，相鄰比較交換
# 若改成Insertion Sort → 內層往左找插入位置，邊找邊移動
# 若改成由大到小排序 → 把 < 改成 >
# 若改成輸出每回合完整陣列 → print(nums) 移到每次swap之後
# 若改成計算總交換次數 → 設swap_count，每次swap時+1，最後輸出

# ==========================================
# 6. Hexadecimal to Decimal
# ==========================================

import sys

# Hexadecimal to Decimal
# 給多行十六進位字串，輸出對應的十進位值
# A-F代表10-15，讀到END停止

for line in sys.stdin:
    line = line.strip()
    if line == "END":                                  # 讀到END結束
        break
    print(int(line, 16))                               # 直接用int轉換十六進位

# 題目變化應對：
# 若改成十進位轉十六進位 → print(hex(n).upper().replace('0X', ''))
# 若改成二進位(base 2)輸入 → int(line, 2)
# 若改成八進位(base 8)輸入 → int(line, 8)
# 若輸入有0x前綴 → line = line.replace('0x','').replace('0X','') 再轉換
# 若輸入有小寫hex → line = line.upper() 再轉換
# 若要輸出固定位數(如8位) → print(f'{int(line,16):08d}')
# 若終止條件改成0或空行 → 把 "END" 換成對應條件即可

# ==========================================
# 7. Prefix to Infix Conversion
# ==========================================

import sys

# Prefix to Infix Conversion
# 給前綴表達式，轉換成完全括號的中綴表達式
# 從右到左讀token：字母直接push，運算子pop兩個合併後push
# 運算子：+ - * /，運算元：單一小寫字母

lines = sys.stdin.read().splitlines()
idx = 0

n = int(lines[idx]); idx += 1                          # 讀測試案例數量

for _ in range(n):
    tokens = lines[idx].split(); idx += 1              # 讀一行前綴表達式
    stack = []
    for token in reversed(tokens):                    # 從右到左讀取token
        if token.isalpha():                            # 字母直接推入堆疊
            stack.append(token)
        else:                                          # 運算子：pop兩個合併
            a = stack.pop()
            b = stack.pop()
            stack.append(f"({a}{token}{b})")          # 組成 (A op B) 推回堆疊
    print(stack[0])                                    # 堆疊最後剩下的就是答案

# 題目變化應對：
# 若改成Infix轉Postfix → 用Shunting-yard演算法，處理運算子優先級
# 若改成Postfix轉Infix → 從左到右讀，字母push，運算子pop兩個合併
# 若改成不加括號只輸出結果 → 把f"({a}{token}{b})"改成直接計算數值
# 若運算元改成數字 → token.isdigit() 取代 token.isalpha()
# 若改成計算表達式的值 → push數值，運算子時pop做實際加減乘除

# ==========================================
# 8. Decode the Receipt
# ==========================================

import sys

# Decode the Receipt
# 給編碼字串，k[...] 表示括號內重複k次，括號可以巢狀
# 輸出解碼後的字串，以及出現最多次的字母（同頻率取字母序最小）
# 重複次數可能超過一位數

def decode(s):
    stack = []
    num = 0
    current = ""
    for ch in s:
        if ch.isdigit():                               # 累積數字（可能多位數）
            num = num * 10 + int(ch)
        elif ch == "[":                                # 進入括號：保存當前狀態
            stack.append((current, num))
            current = ""
            num = 0
        elif ch == "]":                                # 離開括號：重複並還原狀態
            prev, repeat = stack.pop()
            current = prev + current * repeat
        else:                                          # 一般字母直接加入
            current += ch
    return current

line = sys.stdin.read().strip()
result = decode(line)                                  # 解碼字串

freq = {}
for ch in result:                                      # 統計每個字母出現次數
    freq[ch] = freq.get(ch, 0) + 1

best = sorted(freq.items(), key=lambda x: (-x[1], x[0]))[0]  # 最多次，同頻取字母序最小

print(result)
print(f"Most frequent: {best[0]} ({best[1]})")

# 題目變化應對：
# 若改成輸出所有字母頻率 → 印出整個freq字典排序後的結果
# 若改成只輸出解碼長度不輸出字串 → print(len(result))
# 若編碼格式改成(k:...) → 把判斷[改成判斷:，]改成)
# 若改成編碼（壓縮）方向 → 找重複子字串，用run-length encoding壓縮
# 若改成統計最少出現的字母 → 把-x[1]改成x[1]

# ==========================================
# 9. Two Sum
# ==========================================

import sys

# Two Sum
# 給一個整數陣列和目標值，找出相加等於目標的兩個元素索引
# 保證只有一組答案，不能用同一個元素兩次
# 用hash map記錄已看過的數字，達到O(n)效率

lines = sys.stdin.read().splitlines()
nums = list(map(int, lines[0].split()))                # 讀取整數陣列
target = int(lines[1])                                 # 讀取目標值

seen = {}                                              # 記錄已看過的數字與索引
for i, num in enumerate(nums):
    complement = target - num                          # 計算需要的配對數字
    if complement in seen:                             # 找到配對直接輸出
        print(f"[{seen[complement]},{i}]")
        break
    seen[num] = i                                      # 記錄當前數字的索引

# 題目變化應對：
# 若改成Three Sum → 外層固定一個數，內層用Two Sum的hash map找另外兩個
# 若改成輸出值而非索引 → 印出 nums[seen[complement]], num
# 若改成可能有多組答案 → 拿掉break，改用list收集所有答案
# 若改成不能排序且要找最小索引對 → 維持hash map做法即可
# 若陣列很大需要加速 → hash map本來就是O(n)，已是最優解

# ==========================================
# 10. GCD & LCM
# ==========================================

import sys
import math

# GCD & LCM
# 給兩個正整數，輸出最大公因數(GCD)和最小公倍數(LCM)
# LCM公式：a * b // gcd(a, b)，避免大數溢位先除再乘

line = sys.stdin.read().strip()
a, b = map(int, line.split())                          # 讀取兩個整數

g = math.gcd(a, b)                                    # 用內建函式算GCD
l = a * b // g                                        # LCM = a*b / GCD

print(g)
print(l)

# 題目變化應對：
# 若改成多個數的GCD → 用 functools.reduce(math.gcd, nums)
# 若改成多個數的LCM → 用 functools.reduce(lambda a,b: a*b//math.gcd(a,b), nums)
# 若不能用內建math.gcd → 自己寫輾轉相除法：while b: a,b = b, a%b; return a
# 若改成輸出互質判斷 → gcd==1 則輸出 "Coprime"
# 若改成分數化簡 → 分子分母各除以gcd即可

# ==========================================
# 11. Decimal to Binary
# ==========================================

import sys

# Decimal to Binary
# 給一個十進位整數，輸出其二進位表示
# 輸出固定10位，不足補0（依Sample Output格式）

n = int(sys.stdin.read().strip())                      # 讀取十進位整數
print(format(n, '010b'))                               # 輸出10位補零的二進位

# 題目變化應對：
# 若改成不固定位數 → print(bin(n).replace('0b',''))
# 若改成八進位輸出 → print(format(n, 'o')) 或 print(oct(n).replace('0o',''))
# 若改成十六進位輸出 → print(format(n, 'X'))
# 若改成二進位輸入轉十進位 → int(line, 2)
# 若改成輸出固定N位 → print(format(n, f'0{N}b'))
# 若改成手動實作不用format → 用 n%2 反覆取餘數，結果反轉輸出

# ==========================================
# 12. String Run-Length Encoding
# ==========================================

import sys

# String Run-Length Encoding
# 給一串小寫字母，輸出run-length編碼
# 連續相同字母壓縮成「字母+次數」，次數為1時不印數字

s = sys.stdin.read().strip()                           # 讀取字串
result = ""
i = 0

while i < len(s):
    ch = s[i]
    count = 1
    while i + count < len(s) and s[i + count] == ch:  # 計算連續相同字母數量
        count += 1
    result += ch if count == 1 else ch + str(count)   # 次數為1不加數字
    i += count                                         # 跳到下一段

print(result)

# 題目變化應對：
# 若改成解碼(RLE decode) → 遇數字累積，遇字母重複該字母count次
# 若改成次數為1也要印數字 → 拿掉 if count == 1 的判斷，統一印 ch+str(count)
# 若改成大小寫混合 → 直接處理，不需要額外轉換
# 若改成輸出壓縮率 → print(len(result) / len(s))
# 若改成找最長連續段 → 記錄最大count和對應字母輸出
