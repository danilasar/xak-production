import React from "react"
import { Button } from "@mui/material"
import style from "./TaskPage.module.css"
import { ArrowBackRounded } from "@mui/icons-material"
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';

const TaskPage = (props) => {
    function createData(input, output) {
        return { input, output };
      }
      
      const rows = Object.entries(props.task.tests);

    return (
        <div className={style.wrapper}>
            <h1><Button onClick={() => {props.setTab("Курсы")}}><ArrowBackRounded /></Button>{props.task.title}</h1>
            
            <div className={style.p}>
                {props.task.description}
            </div>
            <div className={style.testsWrapper}>
            <TableContainer component={Paper}>
      <Table sx={{ minWidth: 650 }} aria-label="simple table">
        <TableHead>
          <TableRow>
            <TableCell align="right">Input</TableCell>
            <TableCell align="right">Output</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {rows.map((row) => (
            <TableRow
              key={row.name}
              sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
            >
              <TableCell align="right">{row.input}</TableCell>
              <TableCell align="right">{row.output}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
            </div>
        </div>
    )
}

export default TaskPage