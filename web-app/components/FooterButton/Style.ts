import styled from "styled-components";

export const Wrapper = styled.div`
  background: var(--primary);
  bottom: 0;
  color: var(--primary-contrast);
  cursor: pointer;
  padding: var(--padding);
  position: sticky;
  text-align: center;

  &:hover {
    background: var(--primary-darken);
  }
`;
