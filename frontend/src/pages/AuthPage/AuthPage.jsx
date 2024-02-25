import React, { useState } from "react"
import style from "./AuthPage.module.css"
import { TextField, IconButton, InputAdornment, FormControl, InputLabel, OutlinedInput, ButtonGroup, Button } from "@mui/material"
import { VisibilityOff, Visibility } from "@mui/icons-material"

const AuthPage = (props) => {
    const [form, setForm] = useState({
        email: "",
        password: "",
    })

    const [showPassword, setShowPassword] = useState(false)

    const handleClickShowPassword = () => setShowPassword((show) => !show);

    const handleMouseDownPassword = (event) => {
        event.preventDefault();
    };

    return (
        <form className={style.form}>
          <h2>Авторизация</h2>
            <TextField id="email" label="Электронная почта" variant="outlined" required fullWidth sx={{ m: 1 }} />
            <FormControl sx={{ m: 1 }} fullWidth required variant="outlined">
          <InputLabel htmlFor="outlined-adornment-password">Пароль</InputLabel>
          <OutlinedInput
            id="outlined-adornment-password"
            type={showPassword ? 'text' : 'password'}
            endAdornment={
              <InputAdornment position="end">
                <IconButton
                  aria-label="toggle password visibility"
                  onClick={handleClickShowPassword}
                  onMouseDown={handleMouseDownPassword}
                    edge="end"
                >
                  {showPassword ? <VisibilityOff /> : <Visibility />}
                </IconButton>
              </InputAdornment>
            }
            label="Password"
          />
        </FormControl>
            <Button variant="contained" sx={{m:2}} fullWidth size="large" color="success">Войти</Button>
            <Button variant="outlined" onClick={() => {props.setTab("reg")}} fullWidth color="info">Нет аккаунта? Зарегистрируйтесь!</Button>
        </form>
    )
}

export default AuthPage
