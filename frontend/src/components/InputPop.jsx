import React, { useEffect, forwardRef } from "react";
import "../styles/InputPop.css";

// Forward ref to input element in InputPop
const InputPop = forwardRef(({ filename, setFilename, setCodeWindows, setShowInput }, ref) => {
  const handleFilenameSubmit = () => {
    if (filename) {
      const extension = filename.split(".").pop();
      const langMap = {
        js: "javascript",
        py: "python",
        cpp: "cpp",
        c: "c",
        ts: "typescript",
        java: "java",
      };
      const lang = langMap[extension] || "plaintext";

      setCodeWindows((prev) => [...prev, { filename, lang }]);
      setFilename("");
      setShowInput(false); 
    }
  };

  useEffect(() => {
    if (ref.current) {
      ref.current.focus(); 
    }
  }, [ref]);

  return (
    <div style={{ position: "absolute", top: "0px", left: "0px", zIndex: 1000 }}>
      <input
        ref={ref} 
        type="text"
        placeholder="Enter filename.ext"
        className="inputPop"
        value={filename}
        onChange={(e) => setFilename(e.target.value)}
        onKeyDown={(e) => {
          if (e.key === "Enter") handleFilenameSubmit();
        }}
      />
    </div>
  );
});

export default InputPop;
