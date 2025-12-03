--- Day 3: Lobby ---
You descend a short staircase, enter the surprisingly vast lobby, and are quickly cleared by the security checkpoint. When you get to the main elevators, however, you discover that each one has a red light above it: they're all offline.

"Sorry about that," an Elf apologizes as she tinkers with a nearby control panel. "Some kind of electrical surge seems to have fried them. I'll try to get them online soon."

You explain your need to get further underground. "Well, you could at least take the escalator down to the printing department, not that you'd get much further than that without the elevators working. That is, you could if the escalator weren't also offline."

"But, don't worry! It's not fried; it just needs power. Maybe you can get it running while I keep working on the elevators."

There are batteries nearby that can supply emergency power to the escalator for just such an occasion. The batteries are each labeled with their joltage rating, a value from 1 to 9. You make a note of their joltage ratings (your puzzle input). For example:

987654321111111
811111111111119
234234234234278
818181911112111
The batteries are arranged into banks; each line of digits in your input corresponds to a single bank of batteries. Within each bank, you need to turn on exactly two batteries; the joltage that the bank produces is equal to the number formed by the digits on the batteries you've turned on. For example, if you have a bank like 12345 and you turn on batteries 2 and 4, the bank would produce 24 jolts. (You cannot rearrange batteries.)

You'll need to find the largest possible joltage each bank can produce. In the above example:

In 987654321111111, you can make the largest joltage possible, 98, by turning on the first two batteries.
In 811111111111119, you can make the largest joltage possible by turning on the batteries labeled 8 and 9, producing 89 jolts.
In 234234234234278, you can make 78 by turning on the last two batteries (marked 7 and 8).
In 818181911112111, the largest joltage you can produce is 92.
The total output joltage is the sum of the maximum joltage from each bank, so in this example, the total output joltage is 98 + 89 + 78 + 92 = 357.

There are many batteries in front of you. Find the maximum joltage possible from each bank; what is the total output joltage?

Your puzzle answer was 17346.

The first half of this puzzle is complete! It provides one gold star: *

---

## Day 3: 로비

### 배경
- 로비 도착 -> 엘리베이터 모두 오프라인
- 에스컬레이터도 오프라인 (전력 필요)
- 배터리로 긴급 전력 공급 가능

### 배터리 설명
- **레이팅**: 각 배터리 1~9 숫자로 표시
- **배치**: 여러 뱅크(bank)로 구성
- **입력**: 각 줄 = 하나의 배터리 뱅크
- **예시**:
  ```
  987654321111111
  811111111111119
  234234234234278
  818181911112111
  ```

### Part 1: 규칙
- 각 뱅크에서 **정확히 2개** 배터리 켜기
- 켠 배터리의 숫자를 순서대로 이어서 숫자 만들기
- **제약**: 배터리 재배치 불가 (순서 유지)
- **목표**: 각 뱅크에서 만들 수 있는 **최대 전압** 구하기

### 예제 분석
- `987654321111111`: 처음 2개 -> **98**
- `811111111111119`: 8과 9 -> **89**
- `234234234234278`: 마지막 2개 (7, 8) -> **78**
- `818181911112111`: 최대 -> **92**

**합계**: 98 + 89 + 78 + 92 = **357**

### 핵심
- 각 뱅크에서 2개 선택해서 최대 숫자 만들기
- 모든 뱅크의 최대값 합 구하기

--- Part Two ---
The escalator doesn't move. The Elf explains that it probably needs more joltage to overcome the static friction of the system and hits the big red "joltage limit safety override" button. You lose count of the number of times she needs to confirm "yes, I'm sure" and decorate the lobby a bit while you wait.

Now, you need to make the largest joltage by turning on exactly twelve batteries within each bank.

The joltage output for the bank is still the number formed by the digits of the batteries you've turned on; the only difference is that now there will be 12 digits in each bank's joltage output instead of two.

Consider again the example from before:

987654321111111
811111111111119
234234234234278
818181911112111
Now, the joltages are much larger:

In 987654321111111, the largest joltage can be found by turning on everything except some 1s at the end to produce 987654321111.
In the digit sequence 811111111111119, the largest joltage can be found by turning on everything except some 1s, producing 811111111119.
In 234234234234278, the largest joltage can be found by turning on everything except a 2 battery, a 3 battery, and another 2 battery near the start to produce 434234234278.
In 818181911112111, the joltage 888911112111 is produced by turning on everything except some 1s near the front.
The total output joltage is now much larger: 987654321111 + 811111111119 + 434234234278 + 888911112111 = 3121910778619.

What is the new total output joltage?

---

## Part 2

### 상황
- Part 1 전압으로도 에스컬레이터 안 움직임
- 정지 마찰력 극복을 위해 더 많은 전압 필요
- 안전 오버라이드 버튼 누름

### 새로운 규칙
- 각 뱅크에서 **정확히 12개** 배터리 켜기
- 켠 배터리의 숫자를 순서대로 이어서 12자리 숫자 만들기
- **목표**: 각 뱅크에서 만들 수 있는 **최대 전압** 구하기

### 예제 분석 (동일한 입력)
- `987654321111111`: 끝의 1들 일부 제외 -> **987654321111**
- `811111111111119`: 중간 1들 일부 제외 -> **811111111119**
- `234234234234278`: 앞의 2, 3, 2 제외 -> **434234234278**
- `818181911112111`: 앞의 1들 일부 제외 -> **888911112111**

**합계**: 987654321111 + 811111111119 + 434234234278 + 888911112111 = **3121910778619**

### 핵심
- 각 뱅크에서 12개 선택해서 최대 숫자 만들기
- 전체 길이에서 (전체길이 - 12)개 제외
- 제외할 숫자들을 선택해서 최대값 만들기