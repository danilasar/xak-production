import React from "react"
import style from "./CourseSearchCard.module.css"
import { Button, Card, CardContent, CardActions, Chip, Stack } from "@mui/material"
import { LockRounded } from "@mui/icons-material"

const CourseSearchCard = (props) => {
    return (
        <Card sx={{ minWidth: 275, m: 1 }} variant="outlined" className={style.card}>
        <CardContent>
           <h1>{props.title}</h1>
           <Stack direction="row" spacing={1}>{props.category.map((item) => <Chip label={item} variant="outlined" size="small" sx={{ m: 1 }}/>)}</Stack>
        </CardContent>
        <CardActions>
            <Button variant="outlined" size="small" disabled={!props.is_open} startIcon={!props.is_open && <LockRounded />} onClick={() => {props.setTab(`course${props.id}`)}}>Перейти к курсу</Button>
        </CardActions>
        </Card>
    )
}

export default CourseSearchCard