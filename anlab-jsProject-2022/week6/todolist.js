document.addEventListener('DOMContentLoaded', () => {
    // 문서 객체 가져오기
    const input = document.querySelector('#todo');
    const todoList = document.querySelector('#todo-list');
    const addButton = document.querySelector('#add-button');

    // 변수 선언
    let keyCount = 0;

    // 함수 선언
    const addTodo = () => {
        // 입력 양식에 내용이 없으면 추가하지 않는다
        if (input.value.trim() === '') {
            alert('할 일을 입력해주세요');
            return;
        }

        // 문서 객체 설정
        const item = document.createElement('div');
        const checkbox = document.createElement('input');
        const text = document.createElement('span');
        const button = document.createElement('button');

        // 문서 객체를 식별할 키를 생성
        const key = keyCount;
        keyCount += 1;

        // item 객체 조작, 추가
        item.setAttribute('data-key', key);
        item.appendChild(checkbox);
        item.appendChild(text);
        item.appendChild(button);
        todoList.appendChild(item);

        // checkbox 객체 조작
        checkbox.type = 'checkbox';
        checkbox.addEventListener('change', (event) => {
            item.style.textDecoration = event.target.checked ? 'line-through' : '';
        })

        // text 객체 조작
        text.textContent = input.value;

        // button 객체 조작
        button.textContent = '삭제';
        button.addEventListener('click', () => {
            removeTodo(key);
        })

        // 이벽 양식의 내용을 비우기
        input.value = '';
    }

    const removeTodo = (key) => {
        // 식별 키로 문서 객체를 제거
        const item = document.querySelector(`[data-key="${key}"]`);
        todoList.removeChild(item);
    }

    // 이벤트 연결
    addButton.addEventListener('click', addTodo);
    input.addEventListener('keyup', (event) => {
        // 입력 양식에서 enter 키를 누르면 바로 addTodo() 함수를 호출
        const ENTER = 13;
        if (event.keyCode === ENTER) {
            addTodo();
        }
    })
})