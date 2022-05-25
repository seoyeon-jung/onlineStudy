// week2_calculate 에서 가져옴

let a = prompt("첫 번째 수를 입력해주세요.");
let b = prompt("두 번째 수를 입력해주세요");

// 덧셈은 형변환 안하면 제대로 되지 않음 (+는 보통 연결연산자로 사용됨)
add = Number(a) + Number(b);

sub = a - b;
mul = a * b;
div = a / b;
re = a % b;

console.log(add);
console.log(sub);
console.log(mul);
console.log(div);
console.log(re);