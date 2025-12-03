--- Day 2: Gift Shop ---
You get inside and take the elevator to its only other stop: the gift shop. "Thank you for visiting the North Pole!" gleefully exclaims a nearby sign. You aren't sure who is even allowed to visit the North Pole, but you know you can access the lobby through here, and from there you can access the rest of the North Pole base.

As you make your way through the surprisingly extensive selection, one of the clerks recognizes you and asks for your help.

As it turns out, one of the younger Elves was playing on a gift shop computer and managed to add a whole bunch of invalid product IDs to their gift shop database! Surely, it would be no trouble for you to identify the invalid product IDs for them, right?

They've even checked most of the product ID ranges already; they only have a few product ID ranges (your puzzle input) that you'll need to check. For example:

11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124
(The ID ranges are wrapped here for legibility; in your input, they appear on a single long line.)

The ranges are separated by commas (,); each range gives its first ID and last ID separated by a dash (-).

Since the young Elf was just doing silly patterns, you can find the invalid IDs by looking for any ID which is made only of some sequence of digits repeated twice. So, 55 (5 twice), 6464 (64 twice), and 123123 (123 twice) would all be invalid IDs.

None of the numbers have leading zeroes; 0101 isn't an ID at all. (101 is a valid ID that you would ignore.)

Your job is to find all of the invalid IDs that appear in the given ranges. In the above example:

11-22 has two invalid IDs, 11 and 22.
95-115 has one invalid ID, 99.
998-1012 has one invalid ID, 1010.
1188511880-1188511890 has one invalid ID, 1188511885.
222220-222224 has one invalid ID, 222222.
1698522-1698528 contains no invalid IDs.
446443-446449 has one invalid ID, 446446.
38593856-38593862 has one invalid ID, 38593859.
The rest of the ranges contain no invalid IDs.
Adding up all the invalid IDs in this example produces 1227775554.

What do you get if you add up all of the invalid IDs?

---

## Day 2: 기념품 가게

### 배경
- 엘리베이터로 기념품 가게 도착
- 직원이 도움 요청

### 문제 상황
- 어린 엘프가 컴퓨터로 장난 -> 잘못된 제품 ID 대량 추가
- 대부분 범위는 이미 확인됨, 몇 개 범위만 확인 필요

### 입력 형식
- **구분자**: 쉼표(`,`)로 범위 구분
- **범위 형식**: `시작ID-끝ID`
- **예시**: `11-22,95-115,998-1012,...`
- (입력은 한 줄로 제공됨)

### Part 1: 무효 ID 규칙
- **조건**: 같은 숫자 시퀀스가 **정확히 2번** 반복
- **예시**:
  - `55` (5 두 번)  ok
  - `6464` (64 두 번)  ok
  - `123123` (123 두 번) ok
- **주의**: 앞에 0 없음 (`0101`은 ID 아님, `101`은 유효)

### 예제 분석
- `11-22`: 무효 ID 2개 (11, 22)
- `95-115`: 무효 ID 1개 (99)
- `998-1012`: 무효 ID 1개 (1010)
- `1188511880-1188511890`: 무효 ID 1개 (1188511885)
- `222220-222224`: 무효 ID 1개 (222222)
- `1698522-1698528`: 무효 ID 없음
- `446443-446449`: 무효 ID 1개 (446446)
- `38593856-38593862`: 무효 ID 1개 (38593859)
- 나머지: 무효 ID 없음

**합계**: 1227775554

---

--- Part Two ---
The clerk quickly discovers that there are still invalid IDs in the ranges in your list. Maybe the young Elf was doing other silly patterns as well?

Now, an ID is invalid if it is made only of some sequence of digits repeated at least twice. So, 12341234 (1234 two times), 123123123 (123 three times), 1212121212 (12 five times), and 1111111 (1 seven times) are all invalid IDs.

From the same example as before:

11-22 still has two invalid IDs, 11 and 22.
95-115 now has two invalid IDs, 99 and 111.
998-1012 now has two invalid IDs, 999 and 1010.
1188511880-1188511890 still has one invalid ID, 1188511885.
222220-222224 still has one invalid ID, 222222.
1698522-1698528 still contains no invalid IDs.
446443-446449 still has one invalid ID, 446446.
38593856-38593862 still has one invalid ID, 38593859.
565653-565659 now has one invalid ID, 565656.
824824821-824824827 now has one invalid ID, 824824824.
2121212118-2121212124 now has one invalid ID, 2121212121.
Adding up all the invalid IDs in this example produces 4174379265.

What do you get if you add up all of the invalid IDs using these new rules?

---

## Part 2

### 상황
- Part 1 결과 확인 -> 여전히 무효 ID 존재
- 어린 엘프가 다른 패턴도 사용했을 가능성

### 새로운 무효 ID 규칙
- **조건**: 같은 숫자 시퀀스가 **최소 2번 이상** 반복
- **예시**:
  - `12341234` (1234 두 번) ok
  - `123123123` (123 세 번) ok
  - `1212121212` (12 다섯 번) ok
  - `1111111` (1 일곱 번) ok

### 예제 분석 (동일한 범위)
- `11-22`: 무효 ID 2개 (11, 22) - 동일
- `95-115`: 무효 ID 2개 (99, **111**) - 추가
- `998-1012`: 무효 ID 2개 (**999**, 1010) - 추가
- `1188511880-1188511890`: 무효 ID 1개 (1188511885) - 동일
- `222220-222224`: 무효 ID 1개 (222222) - 동일
- `1698522-1698528`: 무효 ID 없음 - 동일
- `446443-446449`: 무효 ID 1개 (446446) - 동일
- `38593856-38593862`: 무효 ID 1개 (38593859) - 동일
- `565653-565659`: 무효 ID 1개 (**565656**) - 추가
- `824824821-824824827`: 무효 ID 1개 (**824824824**) - 추가
- `2121212118-2121212124`: 무효 ID 1개 (**2121212121**) - 추가

**합계**: 4174379265

