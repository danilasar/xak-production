import React from "react"
import style from "./CoursePage.module.css"
import { Stack,
         Chip,
         Button } from "@mui/material"
import { ArrowBackRounded, ErrorOutlineRounded } from "@mui/icons-material"
import TaskSearchCard from "../../components/TaskSearchCard/TaskSearchCard"

const CoursePage = (props) => {
    return (
        <div className={style.wrapper}>
            <h1><Button onClick={() => {props.setTab("Курсы")}}><ArrowBackRounded /></Button>{props.course.title}</h1>
            <p className={style.p}>
                Теги:&nbsp;
                <Stack direction="row" spacing={1}>{props.course.category.map((item) => <Chip label={item} variant="outlined" size="small" sx={{ m: 1 }}/>)}</Stack>    
            </p>
            <div className={style.p}>
                {props.course.description}
            </div>
            <div className={style.tasksWrapper}>
                {props.course.tasks && props.course.tasks.map((item) => <TaskSearchCard parentID={props.course.id} setTab={props.setTab} value={item.title} {...item} />)}
            </div>
        </div>
    )
}

export default CoursePage