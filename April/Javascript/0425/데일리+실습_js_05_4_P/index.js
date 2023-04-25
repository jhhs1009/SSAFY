/* 
  아래에 코드를 작성해주세요.
*/

const keyword = document.querySelector('input')
const search = document.querySelector('button')

function fetchAlbums(page, limit) {
  page = 1
  limit = 10
  alert('확인!')
}

search.addEventListener('click', fetchAlbums)

const url = '/2.0/?method=album.search&album=believe&api_key=529ad6960af792a92fd29962a4cdbb6d&format=json'

