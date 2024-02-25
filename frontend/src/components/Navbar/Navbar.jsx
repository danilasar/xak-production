import style from "./Navbar.module.css"
import { Button, Avatar, Menu, MenuItem } from "@mui/material"
import { lightBlue, grey } from "@mui/material/colors"
import { DataObjectRounded,
         LockOpenRounded,
         PersonRounded } from "@mui/icons-material"
import { useState } from "react"

const Navbar = (props) => {
    const [anchorEl, setAnchorEl] = useState(null)
    const open = Boolean(anchorEl)

    const handleLogout = (event) => {
        props.setUser(null)
    }

    const handleAuth = () => {
        props.onClick("auth")
    }

    const handleReg = () => {
        props.onClick("reg")
    }

    const handleClick = (event) => {
        setAnchorEl(event.currentTarget);
    };
    
    const handleClose = (section) => {
        setAnchorEl(null);
    };

    return (
        <nav className={style.navbar} color={lightBlue[700]}>
            <div className={style.brand}>
                <Avatar variant="rounded" sx={{ bgcolor: lightBlue[700] }}>
                    <DataObjectRounded />
                </Avatar>
                <b className="buttonDesc">InSchool</b>
            </div>
            
            <ul className={style.items}>
            {props.tabs.map((item) => <Button className={`${item[0] !== props.current && style.outlined}`}
                            variant={item[0] === props.current ? "contained" : "outlined"}
                            onClick={() => props.onClick(item[0])} startIcon={item[1]}>
                    <span className="buttonDesc">{item[0]}</span>   
                </Button>)}
            </ul>

            <ul className={style.items}>
                {!props.sessionUser && <><Button variant="contained"
                                        className={style.outlined}
                                        id="userAuthToggler"
                                        aria-controls={open ? 'basic-auth' : undefined}
                                        aria-haspopup="true"
                                        aria-expanded={open ? 'true' : undefined}
                                        onClick={handleClick}
                                        startIcon={<LockOpenRounded />}>
                                            Авторизация
                                            </Button>
                                    <Menu anchorEl={anchorEl}
                                        open={open}
                                        onClose={handleClose}
                                        MenuListProps={{'aria-labelledby': 'userAuthToggler'}}>
                                    <MenuItem onClick={() => {handleClose("Вход");handleAuth("Вход")}}>Вход</MenuItem>
                                    <MenuItem onClick={() => {handleClose("Регистрация");handleReg("Регистрация")}}>Регистрация</MenuItem>
                                    </Menu></>}
                {props.sessionUser && <>
        <Button variant="contained"
                id="userInfoToggler"
                className={style.outlined}
                aria-controls={open ? 'basic-menu' : undefined}
                aria-haspopup="true"
                aria-expanded={open ? 'true' : undefined}
                onClick={handleClick}
                startIcon={<PersonRounded />}>
        <span className="buttonDesc">{props.sessionUser.username}</span>
        </Button>
        <Menu anchorEl={anchorEl}
              open={open}
              onClose={handleClose}
              MenuListProps={{'aria-labelledby': 'userInfoToggler'}}>
        <MenuItem onClick={() => {handleClose("Мой профиль");props.onClick("Мой профиль")}}>Мой профиль</MenuItem>
        <MenuItem onClick={() => {handleClose("Мои курсы");props.onClick("Мои курсы")}} divider>Мои курсы</MenuItem>
        <MenuItem onClick={() => {handleClose("Выйти");handleLogout()}}>Выйти</MenuItem>
        </Menu></>}
            </ul>    
        </nav>
    )
}

export default Navbar