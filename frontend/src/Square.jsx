import React, {useState} from "react";

const Square = () => {
    const [value, setValue] = useState(null)
    return (
        <button className="square" onClick={() => console.log('клик')}>
          {value}
        </button>
      );
}

export default Square