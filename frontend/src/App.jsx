import React, { useState, useEffect, useRef } from "react";
import "./index.css";
import "./App.css";
import CodeWindow from "./components/CodeWindow";
import InputPop from "./components/InputPop";
import Instruc from "./components/Instruc";

function App() {
  const [codeWindows, setCodeWindows] = useState([]);
  const [showInput, setShowInput] = useState(false);
  const [filename, setFilename] = useState("");
  const inputRef = useRef(null);

  const handleKeyPress = (e) => {
    if (e.ctrlKey && e.key === "q") {
      setShowInput((prev) => !prev);
      setFilename("");
    }
  };

  const closeCodeWindow = (filename) => {
    setCodeWindows((prevWindows) =>
      prevWindows.filter((win) => win.filename !== filename)
    );
  };

  useEffect(() => {
    window.addEventListener("keydown", handleKeyPress);
    return () => window.removeEventListener("keydown", handleKeyPress);
  }, []);

  return (
    <div className="App">
      {codeWindows.length === 0 && <Instruc />}
      {showInput && (
        <InputPop
          ref={inputRef}
          filename={filename}
          setFilename={setFilename}
          setCodeWindows={setCodeWindows}
          setShowInput={setShowInput}
        />
      )}

      {codeWindows.map((window, index) => (
        <div
          key={index}
          style={{
            display: "inline-block",
          }}
        >
          <CodeWindow
            filename={window.filename}
            lang={window.lang}
            closeCodeWindow={() => closeCodeWindow(window.filename)}
          />
        </div>
      ))}
    </div>
  );
}

export default App;
