import { createGlobalStyle } from "styled-components";

export default createGlobalStyle`
:root {
  --font-size-base: 1.6rem;

  --header-bg: #fff;
  --body-bg: #fff;
  --top-bg: #fafafa;

  --text-color: #333;
  --text-muted: #666;

  --primary: #00b8d4;
  --primary-darken: #00a2bb;
  --primary-contrast: #fff;

  --divider: #e9e9e9;

  --padding: 2rem;
  --margin: 3rem;
}


  *,
  *::before,
  *::after {
    box-sizing: border-box;
    outline: 0;
  }

  html,
  body,
  #__next {
    font-family: -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Oxygen,
      Ubuntu, Cantarell, Fira Sans, Droid Sans, Helvetica Neue, sans-serif;
    background-color: var(--body-bg);
    color: var(--text-color);
    font-size: 10px;
    font-weight: 300;
    height: 100%;
    margin: 0;
    min-height: 100%;
    overflow-x: hidden;
    padding: 0;
  }

  body,
  #__next{
    font-size: var(--font-size-base);
  }

  #__next {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }

  a {
    text-decoration: none;
  }

`;
