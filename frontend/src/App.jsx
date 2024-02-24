import React, { useEffect, useState } from 'react'
import { Button } from '@mui/material'
import './App.css'
import Navbar from "./components/Navbar/Navbar"
import HomePage from './pages/HomePage/HomePage'
import { HomeRounded, SchoolRounded, LeaderboardRounded } from '@mui/icons-material'

const App = () => {
  const [tab, setTab] = useState("Главная")
  const [user, setUser] = useState({
    id: 1,
    role: 1,
    username: "gryazniy_abobus228",
    password: "jopaspisey228"
  })

  /*useEffect(() => {
    const handleUserChanged = () => {
      setUser(fetch(null))
    }
  })*/

  const testUser = {
    id: 1,
    role: 1,
    username: "gryazniy_abobus228",
    password: "jopaspisey228"
  }

  const handleAuth = () => {
    alert("Never gonna give you up")
  }

  return (
    <main>
      <Navbar current={tab} 
              onClick={setTab} 
              tabs={[["Главная", <HomeRounded />], ["Мои курсы", <SchoolRounded />], ["Лидерборды", <LeaderboardRounded />]]}
              sessionUser={user}
              handleAuth={handleAuth}/>
      <pre>{tab}</pre>
      { tab === "Главная" && <HomePage /> }
    </main>
  )
}

export default App
