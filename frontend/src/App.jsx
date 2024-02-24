import './App.css';
import React from "react";
import { render } from 'react-dom';
import { ChakraProvider } from "@chakra-ui/react";

import Header from "./components/Header";
import Button from './components/Button';
import Todos from "./components/Todos";

const App = () => {
  return (
    <ChakraProvider>
        <Header />
        <Todos />
    </ChakraProvider>
  )
}

export default App