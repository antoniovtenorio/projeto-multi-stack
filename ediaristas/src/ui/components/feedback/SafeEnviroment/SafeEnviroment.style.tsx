import { styled } from "@material-ui/core/styles";

export const SafeEnviromentContainer = styled("div")`
  color: ${({ theme }) => theme.palette.text.secondary};
  background-color: ${({ theme }) => theme.palette.background.default};
  text-align: right;
  padding-right: ${({ theme }) => theme.spacing(2)} 0;
  font-size: 12px;
`;
