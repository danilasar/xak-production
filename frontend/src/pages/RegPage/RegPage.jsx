import React, { useState } from "react"
import style from "./RegPage.module.css"
import { TextField,
         IconButton,
         InputAdornment,
         FormControl,
         InputLabel, 
         OutlinedInput,
         ButtonGroup,
         Stack,
         Button,
         Select,
        MenuItem} from "@mui/material"
import { VisibilityOff, Visibility } from "@mui/icons-material"

const RegPage = (props) => {
    const [form, setForm] = useState({
        email: "",
        surname: "",
        name: "",
        patronymic: "",
        role: 0,
        password: "",
        langs: "",
        gradeYear: 1,
        orgCode: ""
    })

    const [passwordEquals, setPasswordEquals] = useState(null)

    const [showPassword, setShowPassword] = useState(false)

    const handleClickShowPassword = () => setShowPassword((show) => !show);

    const handleMouseDownPassword = (event) => {
        event.preventDefault();
    };

    const handleChange = (event) => {
        setForm({...form, role: event.target.value});
      };

    return (
        <form className={style.form}>
            <h2>Регистрация</h2>
            <TextField id="email" label="Электронная почта" variant="outlined" onChange={(event) => {setForm({...form, email: event.target.value})}} required fullWidth sx={{ m: 1 }} />
            <TextField id="surname" onChange={(event) => {setForm({...form, surname: event.target.value})}} label="Фамилия" variant="outlined" required fullWidth sx={{ m: 1 }} />
            <TextField id="name" onChange={(event) => {setForm({...form, name: event.target.value})}} label="Имя" variant="outlined" required fullWidth sx={{ m: 1 }} />
            <TextField id="patronymic" onChange={(event) => {setForm({...form, patronymic: event.target.value})}} label="Отчество" variant="outlined" required fullWidth sx={{ m: 1 }} />
            <FormControl sx={{ m: 1 }} fullWidth required variant="outlined">
          <InputLabel htmlFor="outlined-adornment-password">Пароль</InputLabel>
          <OutlinedInput onChange={(event) => {setForm({...form, password: event.target.value})}}
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
            label="Пароль"
          />
        </FormControl>
        <FormControl sx={{ m: 2 }} fullWidth required variant="outlined">
        <InputLabel htmlFor="outlined-adornment-password">Повторите пароль</InputLabel>
          <OutlinedInput
            id="outlined-adornment-password"
            value={passwordEquals}
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
            label="Повторите пароль"
          />
        </FormControl>
        <FormControl fullWidth>
            <InputLabel id="demo-simple-select-label">Кто вы?</InputLabel>
            <Select
                labelId="demo-simple-select-label"
                id="demo-simple-select"
                value={form.role}
                label="Кто вы?"
                onChange={handleChange}
            >
                <MenuItem value={0}>Я студент</MenuItem>
                <MenuItem value={1}>Я преподаватель</MenuItem>
                <MenuItem value={2}>Я организация</MenuItem>
            </Select>
            </FormControl>
            { form.role === 0 && <Stack fullWidth direction="row" spacing={2} sx={{marginTop:2, marginBottom:2, padding:0, marginLeft:0, marginRight:0}}>
                <TextField id="outlined-basic" fullWidth label={"Любимые технологии (через \",\")"} variant="outlined" onChange={(event) => {setForm({...form, langs: event.target.value})}} />
                <TextField id="outlined-basic" fullWidth label={"Курс"} variant="outlined" onChange={(event) => {setForm({...form, gradeYear: event.target.value})}} />
            </Stack> }
            { form.role === 1 && <Stack fullWidth direction="row" spacing={2} sx={{marginTop:2, marginBottom:2, padding:0, marginLeft:0, marginRight:0}}>
                <TextField id="outlined-basic" fullWidth label={"Код организации"} variant="outlined" onChange={(event) => {setForm({...form, orgCode: event.target.value})}} />
            </Stack> }
            { form.role === 2 && <Stack fullWidth direction="row" spacing={2} sx={{marginTop:2, marginBottom:2, padding:0, marginLeft:0, marginRight:0}}>
                <h1>В разработке. Свяжитесь с нами по почте: danila.sar@ya.ru</h1>
            </Stack> }
            <Button variant="contained" sx={{m:1}} disabled={form.role === 2} fullWidth size="large" color="success">Регистрация</Button>
            <Button variant="outlined" onClick={() => {props.setTab("auth")}} fullWidth color="info">Уже есть аккаунт? Войти!</Button>
            {/* <pre>{JSON.stringify(form, ";", 2)}</pre> */}
        </form>
    )
}

export default RegPage
