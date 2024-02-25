import React from "react"
import style from "./TaskSearchCard.module.css"
import { Button, Card, CardContent, CardActions, Chip, Stack } from "@mui/material"
import { LockRounded } from "@mui/icons-material"

const TaskSearchCard = (props) => {
    return (
        <Card sx={{ m: 1, p: 0 }} variant="outlined" size="small" className={style.card}>
        <CardContent>
           <h1>{props.title}</h1>
           <p>{props.description}</p>
        </CardContent>
        <CardActions>
            <Button variant="outlined" size="small" onClick={() => {props.setTab(`course${props.parentID}task${props.id}`)}}>Решить</Button>
        </CardActions>
        </Card>
    )
}

export default TaskSearchCard