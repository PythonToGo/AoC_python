--- Day 1: Secret Entrance ---
The Elves have good news and bad news.

The good news is that they've discovered project management! This has given them the tools they need to prevent their usual Christmas emergency. For example, they now know that the North Pole decorations need to be finished soon so that other critical tasks can start on time.

The bad news is that they've realized they have a different emergency: according to their resource planning, none of them have any time left to decorate the North Pole!

To save Christmas, the Elves need you to finish decorating the North Pole by December 12th.

Collect stars by solving puzzles. Two puzzles will be made available on each day; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

You arrive at the secret entrance to the North Pole base ready to start decorating. Unfortunately, the password seems to have been changed, so you can't get in. A document taped to the wall helpfully explains:

"Due to new security protocols, the password is locked in the safe below. Please see the attached document for the new combination."

The safe has a dial with only an arrow on it; around the dial are the numbers 0 through 99 in order. As you turn the dial, it makes a small click noise as it reaches each number.

The attached document (your puzzle input) contains a sequence of rotations, one per line, which tell you how to open the safe. A rotation starts with an L or R which indicates whether the rotation should be to the left (toward lower numbers) or to the right (toward higher numbers). Then, the rotation has a distance value which indicates how many clicks the dial should be rotated in that direction.

So, if the dial were pointing at 11, a rotation of R8 would cause the dial to point at 19. After that, a rotation of L19 would cause it to point at 0.

Because the dial is a circle, turning the dial left from 0 one click makes it point at 99. Similarly, turning the dial right from 99 one click makes it point at 0.

So, if the dial were pointing at 5, a rotation of L10 would cause it to point at 95. After that, a rotation of R5 could cause it to point at 0.

The dial starts by pointing at 50.

You could follow the instructions, but your recent required official North Pole secret entrance security training seminar taught you that the safe is actually a decoy. The actual password is the number of times the dial is left pointing at 0 after any rotation in the sequence.

For example, suppose the attached document contained the following rotations:

L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
Following these rotations would cause the dial to move as follows:

The dial starts by pointing at 50.
The dial is rotated L68 to point at 82.
The dial is rotated L30 to point at 52.
The dial is rotated R48 to point at 0.
The dial is rotated L5 to point at 95.
The dial is rotated R60 to point at 55.
The dial is rotated L55 to point at 0.
The dial is rotated L1 to point at 99.
The dial is rotated L99 to point at 0.
The dial is rotated R14 to point at 14.
The dial is rotated L82 to point at 32.
Because the dial points at 0 a total of three times during this process, the password in this example is 3.

Analyze the rotations in your attached document. What's the actual password to open the door?

---

## Day 1: 비밀 입구

### 배경
- 엘프들: 프로젝트 관리 발견 -> 크리스마스 비상사태 예방 도구 확보
- 하지만 새로운 비상사태: 북극 장식할 시간 없음
- 목표: 12월 12일까지 북극 장식 완료
- 퍼즐: 매일 2개, 별 수집

### 문제 상황
- 북극 기지 비밀 입구 도착했는데, 비밀번호 변경되서 들어갈 수 없음 "비밀번호는 금고에 잠겨잇음, 첨부 문서 참조"

### 다이얼 설명
- **구조**: 화살표 + 0~99 숫자 원형 배열
- **동작**: 회전 시 각 숫자마다 클릭 소리
- **시작 위치**: 50

### 회전 명령
- **형식**: `L` 또는 `R` + 거리값
  - `L`: 왼쪽 (낮은 숫자)
  - `R`: 오른쪽 (높은 숫자)
- **예시**:
  - 11에서 `R8` → 19
  - 그 후 `L19` → 0

### 원형 처리
- 0에서 왼쪽 1클릭 → 99
- 99에서 오른쪽 1클릭 → 0
- **예시**: 5에서 `L10` → 95, 그 후 `R5` → 0

### 실제 비밀번호 (Part 1)
- 금고는 함정 (보안 훈련에서 배움)
- **비밀번호**: 회전 시퀀스에서 **회전 후** 다이얼이 0을 가리키는 횟수

### 예제
```
L68, L30, R48, L5, R60, L55, L1, L99, R14, L82
```

**회전 과정**:
- 시작: 50
- L68 → 82
- L30 → 52
- R48 → **0** ✓
- L5 → 95
- R60 → 55
- L55 → **0** ✓
- L1 → 99
- L99 → **0** ✓
- R14 → 14
- L82 → 32

**결과**: 0을 가리킨 횟수 = **3**



--- Part Two ---
You're sure that's the right password, but the door won't open. You knock, but nobody answers. You build a snowman while you think.

As you're rolling the snowballs for your snowman, you find another security document that must have fallen into the snow:

"Due to newer security protocols, please use password method 0x434C49434B until further notice."

You remember from the training seminar that "method 0x434C49434B" means you're actually supposed to count the number of times any click causes the dial to point at 0, regardless of whether it happens during a rotation or at the end of one.

Following the same rotations as in the above example, the dial points at zero a few extra times during its rotations:

The dial starts by pointing at 50.
The dial is rotated L68 to point at 82; during this rotation, it points at 0 once.
The dial is rotated L30 to point at 52.
The dial is rotated R48 to point at 0.
The dial is rotated L5 to point at 95.
The dial is rotated R60 to point at 55; during this rotation, it points at 0 once.
The dial is rotated L55 to point at 0.
The dial is rotated L1 to point at 99.
The dial is rotated L99 to point at 0.
The dial is rotated R14 to point at 14.
The dial is rotated L82 to point at 32; during this rotation, it points at 0 once.
In this example, the dial points at 0 three times at the end of a rotation, plus three more times during a rotation. So, in this example, the new password would be 6.

Be careful: if the dial were pointing at 50, a single rotation like R1000 would cause the dial to point at 0 ten times before returning back to 50!

Using password method 0x434C49434B, what is the password to open the door?

---

## Part 2

### 상황
- Part 1 비밀번호 입력 -> 문 안 열림
- 눈사람 만들다가 새로운 보안 문서 발견

### 새로운 비밀번호 방법
- **방법**: `0x434C49434B`
- **의미**: 회전 **중** 또는 회전 **끝** 상관없이 모든 클릭에서 0을 가리키는 횟수 세기

### 예제 (동일한 회전)
**회전 과정**:
- 시작: 50
- L68 → 82 (회전 중 **0** 1회) ✓
- L30 → 52
- R48 → **0** ✓
- L5 → 95
- R60 → 55 (회전 중 **0** 1회) ✓
- L55 → **0** ✓
- L1 → 99
- L99 → **0** ✓
- R14 → 14
- L82 → 32 (회전 중 **0** 1회) ✓

**결과**:
- 회전 끝에 0: 3회
- 회전 중 0: 3회
- **총합**: **6**

### 주의사항
- 예: 50에서 `R1000` 회전
  - 50 → 51 → ... → 99 → **0** → 1 → ... → 49 → 50
  - 0을 가리키는 횟수: **10회** (1000 / 100 = 10)

