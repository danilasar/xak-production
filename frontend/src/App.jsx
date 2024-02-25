import React, { useEffect, useState } from 'react'
import { Button } from '@mui/material'
import './App.css'
import Navbar from "./components/Navbar/Navbar"
import AuthPage from './pages/AuthPage/AuthPage'
import RegPage from './pages/RegPage/RegPage'
import HomePage from "./pages/HomePage/HomePage"
import ProfilePage from './pages/ProfilePage/ProfilePage'
import CoursesPage from './pages/CoursesPage/CoursesPage'
import CoursePage from './pages/CoursePage/CoursePage'
import MyCoursesPage from './pages/MyCoursesPage/MyCoursesPage'
import LeaderboardPage from './pages/LeaderboardPage/LeaderboardPage'
import { HomeRounded, SchoolRounded, LeaderboardRounded } from '@mui/icons-material'

const App = () => {
  const [tab, setTab] = useState("Курсы")
  const [user, setUser] = useState(null)

/*{
    id: 1,
    role: 1,
    username: "gryazniy_abobus228",
    password: "jopaspisey228"
  } */

  /*useEffect(() => {
    const handleUserChanged = () => {
      setUser(fetch(null))
    }
  })*/

  const handleAuth = () => {
    setTab("auth")
  }

  const coursesList = [
    {
        id: 1,
        owner_id: 156,
        title: "Курс от Блиновской",
        is_open: true,
        category: ["Scam", "Test"]
    }, {
        id: 2,
        owner_id: 74,
        title: "Боль вышмат ",
        is_open: true,
        category: ["Dogs", "Zoo"]
    }, {
      id: 4,
      owner_id: 4545,
      title: "Марафон желаний",
      is_open: true,
      category: ["Marafosha"]
  }
]

  return (
    <>
      <Navbar current={tab}
              setUser={setUser}
              onClick={setTab} 
              tabs={[["Главная", <HomeRounded />], ["Курсы", <SchoolRounded />], ["Лидерборды", <LeaderboardRounded />]]}
              sessionUser={user}
              handleAuth={handleAuth}/>
      <pre>{tab}</pre>
      <pre>{ ~String('course').indexOf(tab) }</pre>
      <main>
      { tab === "Главная" && <HomePage /> }
      { tab === "Курсы" && <CoursesPage coursesList={coursesList} setTab={setTab}/> }
      { tab === "Лидерборды" && <LeaderboardPage /> }
      { tab === "Мой профиль" && <ProfilePage /> }
      { tab === "Мои курсы" && <MyCoursesPage /> }
      { tab === "auth" && <AuthPage setTab={setTab} />}
      { tab === "reg" && <RegPage setTab={setTab} />}
      { /^course\d+$/.test(tab) && <CoursePage course={coursesList.filter((item) => String(item.id) === tab.slice(6))[0]} /> }
      </main>
    </>
  )
}

export default App
