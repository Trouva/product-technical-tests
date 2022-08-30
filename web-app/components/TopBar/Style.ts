import styled from "styled-components";

export const Wrapper = styled.div`
  background: var(--top-bg);
  border-bottom: 1px solid var(--divider);
  cursor: pointer;
  display: flex;
  position: sticky;
  top: 0;
  z-index: 10;
`;

export const Content = styled.div`
  padding: calc(var(--padding) / 2) 0;
`;

export const Icon = styled.div`
  line-height: 2rem;
  padding: calc(var(--padding) / 2) var(--margin);
  text-align: center;

  &:hover {
    background: rgba(0, 0, 0, 0.025);
  }
`;
