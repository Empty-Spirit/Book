import { post, get } from "./request";

let api = {
  user: {
    login: post("/user/userList.php")
  }
}

export default api